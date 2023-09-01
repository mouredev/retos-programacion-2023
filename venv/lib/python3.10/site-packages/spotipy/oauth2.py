# -*- coding: utf-8 -*-

__all__ = [
    "SpotifyClientCredentials",
    "SpotifyOAuth",
    "SpotifyOauthError",
    "SpotifyStateError",
    "SpotifyImplicitGrant",
    "SpotifyPKCE"
]

import base64
import logging
import os
import time
import warnings
import webbrowser

import requests
# Workaround to support both python 2 & 3
import six
import six.moves.urllib.parse as urllibparse
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from six.moves.urllib_parse import parse_qsl, urlparse

from spotipy.cache_handler import CacheFileHandler, CacheHandler
from spotipy.util import CLIENT_CREDS_ENV_VARS, get_host_port, normalize_scope

logger = logging.getLogger(__name__)


class SpotifyOauthError(Exception):
    """ Error during Auth Code or Implicit Grant flow """

    def __init__(self, message, error=None, error_description=None, *args, **kwargs):
        self.error = error
        self.error_description = error_description
        self.__dict__.update(kwargs)
        super(SpotifyOauthError, self).__init__(message, *args, **kwargs)


class SpotifyStateError(SpotifyOauthError):
    """ The state sent and state received were different """

    def __init__(self, local_state=None, remote_state=None, message=None,
                 error=None, error_description=None, *args, **kwargs):
        if not message:
            message = ("Expected " + local_state + " but recieved "
                       + remote_state)
        super(SpotifyOauthError, self).__init__(message, error,
                                                error_description, *args,
                                                **kwargs)


def _make_authorization_headers(client_id, client_secret):
    auth_header = base64.b64encode(
        six.text_type(client_id + ":" + client_secret).encode("ascii")
    )
    return {"Authorization": "Basic %s" % auth_header.decode("ascii")}


def _ensure_value(value, env_key):
    env_val = CLIENT_CREDS_ENV_VARS[env_key]
    _val = value or os.getenv(env_val)
    if _val is None:
        msg = "No %s. Pass it or set a %s environment variable." % (
            env_key,
            env_val,
        )
        raise SpotifyOauthError(msg)
    return _val


class SpotifyAuthBase(object):
    def __init__(self, requests_session):
        if isinstance(requests_session, requests.Session):
            self._session = requests_session
        else:
            if requests_session:  # Build a new session.
                self._session = requests.Session()
            else:  # Use the Requests API module as a "session".
                from requests import api
                self._session = api

    def _normalize_scope(self, scope):
        return normalize_scope(scope)

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, val):
        self._client_id = _ensure_value(val, "client_id")

    @property
    def client_secret(self):
        return self._client_secret

    @client_secret.setter
    def client_secret(self, val):
        self._client_secret = _ensure_value(val, "client_secret")

    @property
    def redirect_uri(self):
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, val):
        self._redirect_uri = _ensure_value(val, "redirect_uri")

    @staticmethod
    def _get_user_input(prompt):
        try:
            return raw_input(prompt)
        except NameError:
            return input(prompt)

    @staticmethod
    def is_token_expired(token_info):
        now = int(time.time())
        return token_info["expires_at"] - now < 60

    @staticmethod
    def _is_scope_subset(needle_scope, haystack_scope):
        needle_scope = set(needle_scope.split()) if needle_scope else set()
        haystack_scope = (
            set(haystack_scope.split()) if haystack_scope else set()
        )
        return needle_scope <= haystack_scope

    def _handle_oauth_error(self, http_error):
        response = http_error.response
        try:
            error_payload = response.json()
            error = error_payload.get('error')
            error_description = error_payload.get('error_description')
        except ValueError:
            # if the response cannot be decoded into JSON (which raises a ValueError),
            # then try to decode it into text

            # if we receive an empty string (which is falsy), then replace it with `None`
            error = response.text or None
            error_description = None

        raise SpotifyOauthError(
            'error: {0}, error_description: {1}'.format(
                error, error_description
            ),
            error=error,
            error_description=error_description
        )

    def __del__(self):
        """Make sure the connection (pool) gets closed"""
        if isinstance(self._session, requests.Session):
            self._session.close()


class SpotifyClientCredentials(SpotifyAuthBase):
    OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

    def __init__(
        self,
        client_id=None,
        client_secret=None,
        proxies=None,
        requests_session=True,
        requests_timeout=None,
        cache_handler=None
    ):
        """
        Creates a Client Credentials Flow Manager.

        The Client Credentials flow is used in server-to-server authentication.
        Only endpoints that do not access user information can be accessed.
        This means that endpoints that require authorization scopes cannot be accessed.
        The advantage, however, of this authorization flow is that it does not require any
        user interaction

        You can either provide a client_id and client_secret to the
        constructor or set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
        environment variables

        Parameters:
             * client_id: Must be supplied or set as environment variable
             * client_secret: Must be supplied or set as environment variable
             * proxies: Optional, proxy for the requests library to route through
             * requests_session: A Requests session
             * requests_timeout: Optional, tell Requests to stop waiting for a response after
                                 a given number of seconds
             * cache_handler: An instance of the `CacheHandler` class to handle
                              getting and saving cached authorization tokens.
                              Optional, will otherwise use `CacheFileHandler`.
                              (takes precedence over `cache_path` and `username`)

        """

        super(SpotifyClientCredentials, self).__init__(requests_session)

        self.client_id = client_id
        self.client_secret = client_secret
        self.proxies = proxies
        self.requests_timeout = requests_timeout
        if cache_handler:
            assert issubclass(cache_handler.__class__, CacheHandler), \
                "cache_handler must be a subclass of CacheHandler: " + str(type(cache_handler)) \
                + " != " + str(CacheHandler)
            self.cache_handler = cache_handler
        else:
            self.cache_handler = CacheFileHandler()

    def get_access_token(self, as_dict=True, check_cache=True):
        """
        If a valid access token is in memory, returns it
        Else fetches a new token and returns it

            Parameters:
            - as_dict - a boolean indicating if returning the access token
                as a token_info dictionary, otherwise it will be returned
                as a string.
        """
        if as_dict:
            warnings.warn(
                "You're using 'as_dict = True'."
                "get_access_token will return the token string directly in future "
                "versions. Please adjust your code accordingly, or use "
                "get_cached_token instead.",
                DeprecationWarning,
                stacklevel=2,
            )

        if check_cache:
            token_info = self.cache_handler.get_cached_token()
            if token_info and not self.is_token_expired(token_info):
                return token_info if as_dict else token_info["access_token"]

        token_info = self._request_access_token()
        token_info = self._add_custom_values_to_token_info(token_info)
        self.cache_handler.save_token_to_cache(token_info)
        return token_info if as_dict else token_info["access_token"]

    def _request_access_token(self):
        """Gets client credentials access token """
        payload = {"grant_type": "client_credentials"}

        headers = _make_authorization_headers(
            self.client_id, self.client_secret
        )

        logger.debug(
            "sending POST request to %s with Headers: %s and Body: %r",
            self.OAUTH_TOKEN_URL, headers, payload
        )

        try:
            response = self._session.post(
                self.OAUTH_TOKEN_URL,
                data=payload,
                headers=headers,
                verify=True,
                proxies=self.proxies,
                timeout=self.requests_timeout,
            )
            response.raise_for_status()
            token_info = response.json()
            return token_info
        except requests.exceptions.HTTPError as http_error:
            self._handle_oauth_error(http_error)

    def _add_custom_values_to_token_info(self, token_info):
        """
        Store some values that aren't directly provided by a Web API
        response.
        """
        token_info["expires_at"] = int(time.time()) + token_info["expires_in"]
        return token_info


class SpotifyOAuth(SpotifyAuthBase):
    """
    Implements Authorization Code Flow for Spotify's OAuth implementation.
    """
    OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
    OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

    def __init__(
            self,
            client_id=None,
            client_secret=None,
            redirect_uri=None,
            state=None,
            scope=None,
            cache_path=None,
            username=None,
            proxies=None,
            show_dialog=False,
            requests_session=True,
            requests_timeout=None,
            open_browser=True,
            cache_handler=None
    ):
        """
        Creates a SpotifyOAuth object

        Parameters:
             * client_id: Must be supplied or set as environment variable
             * client_secret: Must be supplied or set as environment variable
             * redirect_uri: Must be supplied or set as environment variable
             * state: Optional, no verification is performed
             * scope: Optional, either a list of scopes or comma separated string of scopes.
                      e.g, "playlist-read-private,playlist-read-collaborative"
             * cache_path: (deprecated) Optional, will otherwise be generated
                           (takes precedence over `username`)
             * username: (deprecated) Optional or set as environment variable
                         (will set `cache_path` to `.cache-{username}`)
             * proxies: Optional, proxy for the requests library to route through
             * show_dialog: Optional, interpreted as boolean
             * requests_session: A Requests session
             * requests_timeout: Optional, tell Requests to stop waiting for a response after
                                 a given number of seconds
             * open_browser: Optional, whether or not the web browser should be opened to
                             authorize a user
             * cache_handler: An instance of the `CacheHandler` class to handle
                              getting and saving cached authorization tokens.
                              Optional, will otherwise use `CacheFileHandler`.
                              (takes precedence over `cache_path` and `username`)
        """

        super(SpotifyOAuth, self).__init__(requests_session)

        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.state = state
        self.scope = self._normalize_scope(scope)
        if username or cache_path:
            warnings.warn("Specifying cache_path or username as arguments to SpotifyOAuth " +
                          "will be deprecated. Instead, please create a CacheFileHandler " +
                          "instance with the desired cache_path and username and pass it " +
                          "to SpotifyOAuth as the cache_handler. For example:\n\n" +
                          "\tfrom spotipy.oauth2 import CacheFileHandler\n" +
                          "\thandler = CacheFileHandler(cache_path=cache_path, " +
                          "username=username)\n" +
                          "\tsp = spotipy.SpotifyOAuth(client_id, client_secret, " +
                          "redirect_uri," +
                          " cache_handler=handler)",
                          DeprecationWarning
                          )
            if cache_handler:
                warnings.warn("A cache_handler has been specified along with a cache_path or " +
                              "username. The cache_path and username arguments will be ignored.")
        if cache_handler:
            assert issubclass(cache_handler.__class__, CacheHandler), \
                "cache_handler must be a subclass of CacheHandler: " + str(type(cache_handler)) \
                + " != " + str(CacheHandler)
            self.cache_handler = cache_handler
        else:
            username = (username or os.getenv(CLIENT_CREDS_ENV_VARS["client_username"]))
            self.cache_handler = CacheFileHandler(
                username=username,
                cache_path=cache_path
            )
        self.proxies = proxies
        self.requests_timeout = requests_timeout
        self.show_dialog = show_dialog
        self.open_browser = open_browser

    def validate_token(self, token_info):
        if token_info is None:
            return None

        # if scopes don't match, then bail
        if "scope" not in token_info or not self._is_scope_subset(
                self.scope, token_info["scope"]
        ):
            return None

        if self.is_token_expired(token_info):
            token_info = self.refresh_access_token(
                token_info["refresh_token"]
            )

        return token_info

    def get_authorize_url(self, state=None):
        """ Gets the URL to use to authorize this app
        """
        payload = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
        }
        if self.scope:
            payload["scope"] = self.scope
        if state is None:
            state = self.state
        if state is not None:
            payload["state"] = state
        if self.show_dialog:
            payload["show_dialog"] = True

        urlparams = urllibparse.urlencode(payload)

        return "%s?%s" % (self.OAUTH_AUTHORIZE_URL, urlparams)

    def parse_response_code(self, url):
        """ Parse the response code in the given response url

            Parameters:
                - url - the response url
        """
        _, code = self.parse_auth_response_url(url)
        if code is None:
            return url
        else:
            return code

    @staticmethod
    def parse_auth_response_url(url):
        query_s = urlparse(url).query
        form = dict(parse_qsl(query_s))
        if "error" in form:
            raise SpotifyOauthError("Received error from auth server: "
                                    "{}".format(form["error"]),
                                    error=form["error"])
        return tuple(form.get(param) for param in ["state", "code"])

    def _make_authorization_headers(self):
        return _make_authorization_headers(self.client_id, self.client_secret)

    def _open_auth_url(self):
        auth_url = self.get_authorize_url()
        try:
            webbrowser.open(auth_url)
            logger.info("Opened %s in your browser", auth_url)
        except webbrowser.Error:
            logger.error("Please navigate here: %s", auth_url)

    def _get_auth_response_interactive(self, open_browser=False):
        if open_browser:
            self._open_auth_url()
            prompt = "Enter the URL you were redirected to: "
        else:
            url = self.get_authorize_url()
            prompt = (
                "Go to the following URL: {}\n"
                "Enter the URL you were redirected to: ".format(url)
            )
        response = self._get_user_input(prompt)
        state, code = SpotifyOAuth.parse_auth_response_url(response)
        if self.state is not None and self.state != state:
            raise SpotifyStateError(self.state, state)
        return code

    def _get_auth_response_local_server(self, redirect_port):
        server = start_local_http_server(redirect_port)
        self._open_auth_url()
        server.handle_request()

        if server.error is not None:
            raise server.error
        elif self.state is not None and server.state != self.state:
            raise SpotifyStateError(self.state, server.state)
        elif server.auth_code is not None:
            return server.auth_code
        else:
            raise SpotifyOauthError("Server listening on localhost has not been accessed")

    def get_auth_response(self, open_browser=None):
        logger.info('User authentication requires interaction with your '
                    'web browser. Once you enter your credentials and '
                    'give authorization, you will be redirected to '
                    'a url.  Paste that url you were directed to to '
                    'complete the authorization.')

        redirect_info = urlparse(self.redirect_uri)
        redirect_host, redirect_port = get_host_port(redirect_info.netloc)

        if open_browser is None:
            open_browser = self.open_browser

        if (
                open_browser
                and redirect_host in ("127.0.0.1", "localhost")
                and redirect_info.scheme == "http"
        ):
            # Only start a local http server if a port is specified
            if redirect_port:
                return self._get_auth_response_local_server(redirect_port)
            else:
                logger.warning('Using `%s` as redirect URI without a port. '
                               'Specify a port (e.g. `%s:8080`) to allow '
                               'automatic retrieval of authentication code '
                               'instead of having to copy and paste '
                               'the URL your browser is redirected to.',
                               redirect_host, redirect_host)

        return self._get_auth_response_interactive(open_browser=open_browser)

    def get_authorization_code(self, response=None):
        if response:
            return self.parse_response_code(response)
        return self.get_auth_response()

    def get_access_token(self, code=None, as_dict=True, check_cache=True):
        """ Gets the access token for the app given the code

            Parameters:
                - code - the response code
                - as_dict - a boolean indicating if returning the access token
                            as a token_info dictionary, otherwise it will be returned
                            as a string.
        """
        if as_dict:
            warnings.warn(
                "You're using 'as_dict = True'."
                "get_access_token will return the token string directly in future "
                "versions. Please adjust your code accordingly, or use "
                "get_cached_token instead.",
                DeprecationWarning,
                stacklevel=2,
            )
        if check_cache:
            token_info = self.validate_token(self.cache_handler.get_cached_token())
            if token_info is not None:
                if self.is_token_expired(token_info):
                    token_info = self.refresh_access_token(
                        token_info["refresh_token"]
                    )
                return token_info if as_dict else token_info["access_token"]

        payload = {
            "redirect_uri": self.redirect_uri,
            "code": code or self.get_auth_response(),
            "grant_type": "authorization_code",
        }
        if self.scope:
            payload["scope"] = self.scope
        if self.state:
            payload["state"] = self.state

        headers = self._make_authorization_headers()

        logger.debug(
            "sending POST request to %s with Headers: %s and Body: %r",
            self.OAUTH_TOKEN_URL, headers, payload
        )

        try:
            response = self._session.post(
                self.OAUTH_TOKEN_URL,
                data=payload,
                headers=headers,
                verify=True,
                proxies=self.proxies,
                timeout=self.requests_timeout,
            )
            response.raise_for_status()
            token_info = response.json()
            token_info = self._add_custom_values_to_token_info(token_info)
            self.cache_handler.save_token_to_cache(token_info)
            return token_info if as_dict else token_info["access_token"]
        except requests.exceptions.HTTPError as http_error:
            self._handle_oauth_error(http_error)

    def refresh_access_token(self, refresh_token):
        payload = {
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        }

        headers = self._make_authorization_headers()

        logger.debug(
            "sending POST request to %s with Headers: %s and Body: %r",
            self.OAUTH_TOKEN_URL, headers, payload
        )

        try:
            response = self._session.post(
                self.OAUTH_TOKEN_URL,
                data=payload,
                headers=headers,
                proxies=self.proxies,
                timeout=self.requests_timeout,
            )
            response.raise_for_status()
            token_info = response.json()
            token_info = self._add_custom_values_to_token_info(token_info)
            if "refresh_token" not in token_info:
                token_info["refresh_token"] = refresh_token
            self.cache_handler.save_token_to_cache(token_info)
            return token_info
        except requests.exceptions.HTTPError as http_error:
            self._handle_oauth_error(http_error)

    def _add_custom_values_to_token_info(self, token_info):
        """
        Store some values that aren't directly provided by a Web API
        response.
        """
        token_info["expires_at"] = int(time.time()) + token_info["expires_in"]
        token_info["scope"] = self.scope
        return token_info

    def get_cached_token(self):
        warnings.warn("Calling get_cached_token directly on the SpotifyOAuth object will be " +
                      "deprecated. Instead, please specify a CacheFileHandler instance as " +
                      "the cache_handler in SpotifyOAuth and use the CacheFileHandler's " +
                      "get_cached_token method. You can replace:\n\tsp.get_cached_token()" +
                      "\n\nWith:\n\tsp.validate_token(sp.cache_handler.get_cached_token())",
                      DeprecationWarning
                      )
        return self.validate_token(self.cache_handler.get_cached_token())

    def _save_token_info(self, token_info):
        warnings.warn("Calling _save_token_info directly on the SpotifyOAuth object will be " +
                      "deprecated. Instead, please specify a CacheFileHandler instance as " +
                      "the cache_handler in SpotifyOAuth and use the CacheFileHandler's " +
                      "save_token_to_cache method.",
                      DeprecationWarning
                      )
        self.cache_handler.save_token_to_cache(token_info)
        return None


class SpotifyPKCE(SpotifyAuthBase):
    """ Implements PKCE Authorization Flow for client apps

    This auth manager enables *user and non-user* endpoints with only
    a client ID, redirect URI, and username. When the app requests
    an access token for the first time, the user is prompted to
    authorize the new client app. After authorizing the app, the client
    app is then given both access and refresh tokens. This is the
    preferred way of authorizing a mobile/desktop client.

    """

    OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
    OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

    def __init__(self,
                 client_id=None,
                 redirect_uri=None,
                 state=None,
                 scope=None,
                 cache_path=None,
                 username=None,
                 proxies=None,
                 requests_timeout=None,
                 requests_session=True,
                 open_browser=True,
                 cache_handler=None):
        """
        Creates Auth Manager with the PKCE Auth flow.

        Parameters:
             * client_id: Must be supplied or set as environment variable
             * redirect_uri: Must be supplied or set as environment variable
             * state: Optional, no verification is performed
             * scope: Optional, either a list of scopes or comma separated string of scopes.
                      e.g, "playlist-read-private,playlist-read-collaborative"
             * cache_path: (deprecated) Optional, will otherwise be generated
                           (takes precedence over `username`)
             * username: (deprecated) Optional or set as environment variable
                         (will set `cache_path` to `.cache-{username}`)
             * proxies: Optional, proxy for the requests library to route through
             * requests_timeout: Optional, tell Requests to stop waiting for a response after
                                 a given number of seconds
             * requests_session: A Requests session
             * open_browser: Optional, whether or not the web browser should be opened to
                             authorize a user
             * cache_handler: An instance of the `CacheHandler` class to handle
                              getting and saving cached authorization tokens.
                              Optional, will otherwise use `CacheFileHandler`.
                              (takes precedence over `cache_path` and `username`)
        """

        super(SpotifyPKCE, self).__init__(requests_session)
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.state = state
        self.scope = self._normalize_scope(scope)
        if username or cache_path:
            warnings.warn("Specifying cache_path or username as arguments to SpotifyPKCE " +
                          "will be deprecated. Instead, please create a CacheFileHandler " +
                          "instance with the desired cache_path and username and pass it " +
                          "to SpotifyPKCE as the cache_handler. For example:\n\n" +
                          "\tfrom spotipy.oauth2 import CacheFileHandler\n" +
                          "\thandler = CacheFileHandler(cache_path=cache_path, " +
                          "username=username)\n" +
                          "\tsp = spotipy.SpotifyImplicitGrant(client_id, client_secret, " +
                          "redirect_uri, cache_handler=handler)",
                          DeprecationWarning
                          )
            if cache_handler:
                warnings.warn("A cache_handler has been specified along with a cache_path or " +
                              "username. The cache_path and username arguments will be ignored.")
        if cache_handler:
            assert issubclass(type(cache_handler), CacheHandler), \
                "type(cache_handler): " + str(type(cache_handler)) + " != " + str(CacheHandler)
            self.cache_handler = cache_handler
        else:
            username = (username or os.getenv(CLIENT_CREDS_ENV_VARS["client_username"]))
            self.cache_handler = CacheFileHandler(
                username=username,
                cache_path=cache_path
            )
        self.proxies = proxies
        self.requests_timeout = requests_timeout

        self._code_challenge_method = "S256"  # Spotify requires SHA256
        self.code_verifier = None
        self.code_challenge = None
        self.authorization_code = None
        self.open_browser = open_browser

    def _get_code_verifier(self):
        """ Spotify PCKE code verifier - See step 1 of the reference guide below
        Reference:
        https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow-with-proof-key-for-code-exchange-pkce
        """
        # Range (33,96) is used to select between 44-128 base64 characters for the
        # next operation. The range looks weird because base64 is 6 bytes
        import random
        length = random.randint(33, 96)

        # The seeded length generates between a 44 and 128 base64 characters encoded string
        try:
            import secrets
            verifier = secrets.token_urlsafe(length)
        except ImportError:  # For python 3.5 support
            import base64
            import os
            rand_bytes = os.urandom(length)
            verifier = base64.urlsafe_b64encode(rand_bytes).decode('utf-8').replace('=', '')
        return verifier

    def _get_code_challenge(self):
        """ Spotify PCKE code challenge - See step 1 of the reference guide below
        Reference:
        https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow-with-proof-key-for-code-exchange-pkce
        """
        import base64
        import hashlib
        code_challenge_digest = hashlib.sha256(self.code_verifier.encode('utf-8')).digest()
        code_challenge = base64.urlsafe_b64encode(code_challenge_digest).decode('utf-8')
        return code_challenge.replace('=', '')

    def get_authorize_url(self, state=None):
        """ Gets the URL to use to authorize this app """
        if not self.code_challenge:
            self.get_pkce_handshake_parameters()
        payload = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "code_challenge_method": self._code_challenge_method,
            "code_challenge": self.code_challenge
        }
        if self.scope:
            payload["scope"] = self.scope
        if state is None:
            state = self.state
        if state is not None:
            payload["state"] = state
        urlparams = urllibparse.urlencode(payload)
        return "%s?%s" % (self.OAUTH_AUTHORIZE_URL, urlparams)

    def _open_auth_url(self, state=None):
        auth_url = self.get_authorize_url(state)
        try:
            webbrowser.open(auth_url)
            logger.info("Opened %s in your browser", auth_url)
        except webbrowser.Error:
            logger.error("Please navigate here: %s", auth_url)

    def _get_auth_response(self, open_browser=None):
        logger.info('User authentication requires interaction with your '
                    'web browser. Once you enter your credentials and '
                    'give authorization, you will be redirected to '
                    'a url.  Paste that url you were directed to to '
                    'complete the authorization.')

        redirect_info = urlparse(self.redirect_uri)
        redirect_host, redirect_port = get_host_port(redirect_info.netloc)

        if open_browser is None:
            open_browser = self.open_browser

        if (
                open_browser
                and redirect_host in ("127.0.0.1", "localhost")
                and redirect_info.scheme == "http"
        ):
            # Only start a local http server if a port is specified
            if redirect_port:
                return self._get_auth_response_local_server(redirect_port)
            else:
                logger.warning('Using `%s` as redirect URI without a port. '
                               'Specify a port (e.g. `%s:8080`) to allow '
                               'automatic retrieval of authentication code '
                               'instead of having to copy and paste '
                               'the URL your browser is redirected to.',
                               redirect_host, redirect_host)
        return self._get_auth_response_interactive(open_browser=open_browser)

    def _get_auth_response_local_server(self, redirect_port):
        server = start_local_http_server(redirect_port)
        self._open_auth_url()
        server.handle_request()

        if self.state is not None and server.state != self.state:
            raise SpotifyStateError(self.state, server.state)

        if server.auth_code is not None:
            return server.auth_code
        elif server.error is not None:
            raise SpotifyOauthError("Received error from OAuth server: {}".format(server.error))
        else:
            raise SpotifyOauthError("Server listening on localhost has not been accessed")

    def _get_auth_response_interactive(self, open_browser=False):
        if open_browser or self.open_browser:
            self._open_auth_url()
            prompt = "Enter the URL you were redirected to: "
        else:
            url = self.get_authorize_url()
            prompt = (
                "Go to the following URL: {}\n"
                "Enter the URL you were redirected to: ".format(url)
            )
        response = self._get_user_input(prompt)
        state, code = self.parse_auth_response_url(response)
        if self.state is not None and self.state != state:
            raise SpotifyStateError(self.state, state)
        return code

    def get_authorization_code(self, response=None):
        if response:
            return self.parse_response_code(response)
        return self._get_auth_response()

    def validate_token(self, token_info):
        if token_info is None:
            return None

        # if scopes don't match, then bail
        if "scope" not in token_info or not self._is_scope_subset(
                self.scope, token_info["scope"]
        ):
            return None

        if self.is_token_expired(token_info):
            token_info = self.refresh_access_token(
                token_info["refresh_token"]
            )

        return token_info

    def _add_custom_values_to_token_info(self, token_info):
        """
        Store some values that aren't directly provided by a Web API
        response.
        """
        token_info["expires_at"] = int(time.time()) + token_info["expires_in"]
        return token_info

    def get_pkce_handshake_parameters(self):
        self.code_verifier = self._get_code_verifier()
        self.code_challenge = self._get_code_challenge()

    def get_access_token(self, code=None, check_cache=True):
        """ Gets the access token for the app

            If the code is not given and no cached token is used, an
            authentication window will be shown to the user to get a new
            code.

            Parameters:
                - code - the response code from authentication
                - check_cache - if true, checks for a locally stored token
                                before requesting a new token
        """

        if check_cache:
            token_info = self.validate_token(self.cache_handler.get_cached_token())
            if token_info is not None:
                if self.is_token_expired(token_info):
                    token_info = self.refresh_access_token(
                        token_info["refresh_token"]
                    )
                return token_info["access_token"]

        if self.code_verifier is None or self.code_challenge is None:
            self.get_pkce_handshake_parameters()

        payload = {
            "client_id": self.client_id,
            "grant_type": "authorization_code",
            "code": code or self.get_authorization_code(),
            "redirect_uri": self.redirect_uri,
            "code_verifier": self.code_verifier
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        logger.debug(
            "sending POST request to %s with Headers: %s and Body: %r",
            self.OAUTH_TOKEN_URL, headers, payload
        )

        try:
            response = self._session.post(
                self.OAUTH_TOKEN_URL,
                data=payload,
                headers=headers,
                verify=True,
                proxies=self.proxies,
                timeout=self.requests_timeout,
            )
            response.raise_for_status()
            token_info = response.json()
            token_info = self._add_custom_values_to_token_info(token_info)
            self.cache_handler.save_token_to_cache(token_info)
            return token_info["access_token"]
        except requests.exceptions.HTTPError as http_error:
            self._handle_oauth_error(http_error)

    def refresh_access_token(self, refresh_token):
        payload = {
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "client_id": self.client_id,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        logger.debug(
            "sending POST request to %s with Headers: %s and Body: %r",
            self.OAUTH_TOKEN_URL, headers, payload
        )

        try:
            response = self._session.post(
                self.OAUTH_TOKEN_URL,
                data=payload,
                headers=headers,
                proxies=self.proxies,
                timeout=self.requests_timeout,
            )
            response.raise_for_status()
            token_info = response.json()
            token_info = self._add_custom_values_to_token_info(token_info)
            if "refresh_token" not in token_info:
                token_info["refresh_token"] = refresh_token
            self.cache_handler.save_token_to_cache(token_info)
            return token_info
        except requests.exceptions.HTTPError as http_error:
            self._handle_oauth_error(http_error)

    def parse_response_code(self, url):
        """ Parse the response code in the given response url

            Parameters:
                - url - the response url
        """
        _, code = self.parse_auth_response_url(url)
        if code is None:
            return url
        else:
            return code

    @staticmethod
    def parse_auth_response_url(url):
        return SpotifyOAuth.parse_auth_response_url(url)

    def get_cached_token(self):
        warnings.warn("Calling get_cached_token directly on the SpotifyPKCE object will be " +
                      "deprecated. Instead, please specify a CacheFileHandler instance as " +
                      "the cache_handler in SpotifyOAuth and use the CacheFileHandler's " +
                      "get_cached_token method. You can replace:\n\tsp.get_cached_token()" +
                      "\n\nWith:\n\tsp.validate_token(sp.cache_handler.get_cached_token())",
                      DeprecationWarning
                      )
        return self.validate_token(self.cache_handler.get_cached_token())

    def _save_token_info(self, token_info):
        warnings.warn("Calling _save_token_info directly on the SpotifyOAuth object will be " +
                      "deprecated. Instead, please specify a CacheFileHandler instance as " +
                      "the cache_handler in SpotifyOAuth and use the CacheFileHandler's " +
                      "save_token_to_cache method.",
                      DeprecationWarning
                      )
        self.cache_handler.save_token_to_cache(token_info)
        return None


class SpotifyImplicitGrant(SpotifyAuthBase):
    """ Implements Implicit Grant Flow for client apps

    This auth manager enables *user and non-user* endpoints with only
    a client secret, redirect uri, and username. The user will need to
    copy and paste a URI from the browser every hour.

    Security Warning
    -----------------
    The OAuth standard no longer recommends the Implicit Grant Flow for
    client-side code. Spotify has implemented the OAuth-suggested PKCE
    extension that removes the need for a client secret in the
    Authentication Code flow. Use the SpotifyPKCE auth manager instead
    of SpotifyImplicitGrant.

    SpotifyPKCE contains all of the functionality of
    SpotifyImplicitGrant, plus automatic response retrieval and
    refreshable tokens. Only a few replacements need to be made:

    * get_auth_response()['access_token'] ->
      get_access_token(get_authorization_code())
    * get_auth_response() ->
      get_access_token(get_authorization_code()); get_cached_token()
    * parse_response_token(url)['access_token'] ->
      get_access_token(parse_response_code(url))
    * parse_response_token(url) ->
      get_access_token(parse_response_code(url)); get_cached_token()

    The security concern in the Implicit Grant flow is that the token is
    returned in the URL and can be intercepted through the browser. A
    request with an authorization code and proof of origin could not be
    easily intercepted without a compromised network.
    """
    OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"

    def __init__(self,
                 client_id=None,
                 redirect_uri=None,
                 state=None,
                 scope=None,
                 cache_path=None,
                 username=None,
                 show_dialog=False,
                 cache_handler=None):
        """ Creates Auth Manager using the Implicit Grant flow

        **See help(SpotifyImplicitGrant) for full Security Warning**

        Parameters
        ----------
        * client_id: Must be supplied or set as environment variable
        * redirect_uri: Must be supplied or set as environment variable
        * state: May be supplied, no verification is performed
        * scope: Optional, either a list of scopes or comma separated string of scopes.
                 e.g, "playlist-read-private,playlist-read-collaborative"
        * cache_handler: An instance of the `CacheHandler` class to handle
                              getting and saving cached authorization tokens.
                              May be supplied, will otherwise use `CacheFileHandler`.
                              (takes precedence over `cache_path` and `username`)
        * cache_path: (deprecated) May be supplied, will otherwise be generated
                      (takes precedence over `username`)
        * username: (deprecated) May be supplied or set as environment variable
                    (will set `cache_path` to `.cache-{username}`)
        * show_dialog: Interpreted as boolean
        """
        logger.warning("The OAuth standard no longer recommends the Implicit "
                       "Grant Flow for client-side code. Use the SpotifyPKCE "
                       "auth manager instead of SpotifyImplicitGrant. For "
                       "more details and a guide to switching, see "
                       "help(SpotifyImplicitGrant).")

        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.state = state
        if username or cache_path:
            warnings.warn("Specifying cache_path or username as arguments to " +
                          "SpotifyImplicitGrant will be deprecated. Instead, please create " +
                          "a CacheFileHandler instance with the desired cache_path and " +
                          "username and pass it to SpotifyImplicitGrant as the " +
                          "cache_handler. For example:\n\n" +
                          "\tfrom spotipy.oauth2 import CacheFileHandler\n" +
                          "\thandler = CacheFileHandler(cache_path=cache_path, " +
                          "username=username)\n" +
                          "\tsp = spotipy.SpotifyImplicitGrant(client_id, client_secret, " +
                          "redirect_uri, cache_handler=handler)",
                          DeprecationWarning
                          )
            if cache_handler:
                warnings.warn("A cache_handler has been specified along with a cache_path or " +
                              "username. The cache_path and username arguments will be ignored.")
        if cache_handler:
            assert issubclass(type(cache_handler), CacheHandler), \
                "type(cache_handler): " + str(type(cache_handler)) + " != " + str(CacheHandler)
            self.cache_handler = cache_handler
        else:
            username = (username or os.getenv(CLIENT_CREDS_ENV_VARS["client_username"]))
            self.cache_handler = CacheFileHandler(
                username=username,
                cache_path=cache_path
            )
        self.scope = self._normalize_scope(scope)
        self.show_dialog = show_dialog
        self._session = None  # As to not break inherited __del__

    def validate_token(self, token_info):
        if token_info is None:
            return None

        # if scopes don't match, then bail
        if "scope" not in token_info or not self._is_scope_subset(
                self.scope, token_info["scope"]
        ):
            return None

        if self.is_token_expired(token_info):
            return None

        return token_info

    def get_access_token(self,
                         state=None,
                         response=None,
                         check_cache=True):
        """ Gets Auth Token from cache (preferred) or user interaction

        Parameters
        ----------
        * state: May be given, overrides (without changing) self.state
        * response: URI with token, can break expiration checks
        * check_cache: Interpreted as boolean
        """
        if check_cache:
            token_info = self.validate_token(self.cache_handler.get_cached_token())
            if not (token_info is None or self.is_token_expired(token_info)):
                return token_info["access_token"]

        if response:
            token_info = self.parse_response_token(response)
        else:
            token_info = self.get_auth_response(state)
        token_info = self._add_custom_values_to_token_info(token_info)
        self.cache_handler.save_token_to_cache(token_info)

        return token_info["access_token"]

    def get_authorize_url(self, state=None):
        """ Gets the URL to use to authorize this app """
        payload = {
            "client_id": self.client_id,
            "response_type": "token",
            "redirect_uri": self.redirect_uri,
        }
        if self.scope:
            payload["scope"] = self.scope
        if state is None:
            state = self.state
        if state is not None:
            payload["state"] = state
        if self.show_dialog:
            payload["show_dialog"] = True

        urlparams = urllibparse.urlencode(payload)

        return "%s?%s" % (self.OAUTH_AUTHORIZE_URL, urlparams)

    def parse_response_token(self, url, state=None):
        """ Parse the response code in the given response url """
        remote_state, token, t_type, exp_in = self.parse_auth_response_url(url)
        if state is None:
            state = self.state
        if state is not None and remote_state != state:
            raise SpotifyStateError(state, remote_state)
        return {"access_token": token, "token_type": t_type,
                "expires_in": exp_in, "state": state}

    @staticmethod
    def parse_auth_response_url(url):
        url_components = urlparse(url)
        fragment_s = url_components.fragment
        query_s = url_components.query
        form = dict(i.split('=') for i
                    in (fragment_s or query_s or url).split('&'))
        if "error" in form:
            raise SpotifyOauthError("Received error from auth server: "
                                    "{}".format(form["error"]),
                                    state=form["state"])
        if "expires_in" in form:
            form["expires_in"] = int(form["expires_in"])
        return tuple(form.get(param) for param in ["state", "access_token",
                                                   "token_type", "expires_in"])

    def _open_auth_url(self, state=None):
        auth_url = self.get_authorize_url(state)
        try:
            webbrowser.open(auth_url)
            logger.info("Opened %s in your browser", auth_url)
        except webbrowser.Error:
            logger.error("Please navigate here: %s", auth_url)

    def get_auth_response(self, state=None):
        """ Gets a new auth **token** with user interaction """
        logger.info('User authentication requires interaction with your '
                    'web browser. Once you enter your credentials and '
                    'give authorization, you will be redirected to '
                    'a url.  Paste that url you were directed to to '
                    'complete the authorization.')

        redirect_info = urlparse(self.redirect_uri)
        redirect_host, redirect_port = get_host_port(redirect_info.netloc)
        # Implicit Grant tokens are returned in a hash fragment
        # which is only available to the browser. Therefore, interactive
        # URL retrieval is required.
        if (redirect_host in ("127.0.0.1", "localhost")
                and redirect_info.scheme == "http" and redirect_port):
            logger.warning('Using a local redirect URI with a '
                           'port, likely expecting automatic '
                           'retrieval. Due to technical limitations, '
                           'the authentication token cannot be '
                           'automatically retrieved and must be '
                           'copied and pasted.')

        self._open_auth_url(state)
        logger.info('Paste that url you were directed to in order to '
                    'complete the authorization')
        response = SpotifyImplicitGrant._get_user_input("Enter the URL you "
                                                        "were redirected to: ")
        return self.parse_response_token(response, state)

    def _add_custom_values_to_token_info(self, token_info):
        """
        Store some values that aren't directly provided by a Web API
        response.
        """
        token_info["expires_at"] = int(time.time()) + token_info["expires_in"]
        token_info["scope"] = self.scope
        return token_info

    def get_cached_token(self):
        warnings.warn("Calling get_cached_token directly on the SpotifyImplicitGrant " +
                      "object will be deprecated. Instead, please specify a " +
                      "CacheFileHandler instance as the cache_handler in SpotifyOAuth " +
                      "and use the CacheFileHandler's get_cached_token method. " +
                      "You can replace:\n\tsp.get_cached_token()" +
                      "\n\nWith:\n\tsp.validate_token(sp.cache_handler.get_cached_token())",
                      DeprecationWarning
                      )
        return self.validate_token(self.cache_handler.get_cached_token())

    def _save_token_info(self, token_info):
        warnings.warn("Calling _save_token_info directly on the SpotifyImplicitGrant " +
                      "object will be deprecated. Instead, please specify a " +
                      "CacheFileHandler instance as the cache_handler in SpotifyOAuth " +
                      "and use the CacheFileHandler's save_token_to_cache method.",
                      DeprecationWarning
                      )
        self.cache_handler.save_token_to_cache(token_info)
        return None


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.server.auth_code = self.server.error = None
        try:
            state, auth_code = SpotifyOAuth.parse_auth_response_url(self.path)
            self.server.state = state
            self.server.auth_code = auth_code
        except SpotifyOauthError as error:
            self.server.error = error

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        if self.server.auth_code:
            status = "successful"
        elif self.server.error:
            status = "failed ({})".format(self.server.error)
        else:
            self._write("<html><body><h1>Invalid request</h1></body></html>")
            return

        self._write("""<html>
<script>
window.close()
</script>
<body>
<h1>Authentication status: {}</h1>
This window can be closed.
<script>
window.close()
</script>
<button class="closeButton" style="cursor: pointer" onclick="window.close();">Close Window</button>
</body>
</html>""".format(status))

    def _write(self, text):
        return self.wfile.write(text.encode("utf-8"))

    def log_message(self, format, *args):
        return


def start_local_http_server(port, handler=RequestHandler):
    server = HTTPServer(("127.0.0.1", port), handler)
    server.allow_reuse_address = True
    server.auth_code = None
    server.auth_token_form = None
    server.error = None
    return server
