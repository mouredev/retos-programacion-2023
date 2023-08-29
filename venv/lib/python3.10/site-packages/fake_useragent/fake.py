import random

from fake_useragent import settings
from fake_useragent.errors import FakeUserAgentError
from fake_useragent.log import logger
from fake_useragent.utils import load, str_types


class FakeUserAgent:
    def __init__(
        self,
        browsers=["chrome", "edge", "firefox", "safari"],
        os=["windows", "macos", "linux"],
        min_percentage=0.0,
        fallback="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        safe_attrs=tuple(),
    ):
        # Check inputs
        assert isinstance(browsers, (list, str)), "browsers must be list or string"
        if isinstance(browsers, str):
            browsers = [browsers]
        self.browsers = browsers

        assert isinstance(os, (list, str)), "OS must be list or string"
        # OS replacement (windows -> win10)
        if isinstance(os, str):
            os = [os]
        self.os = [
            settings.OS_REPLACEMENTS[os_name]
            if os_name in settings.OS_REPLACEMENTS
            else os_name
            for os_name in os
        ]

        assert isinstance(
            min_percentage, float
        ), "Minimum usage percentage must be float"
        self.min_percentage = min_percentage

        assert isinstance(fallback, str), "fallback must be string"
        self.fallback = fallback

        assert isinstance(
            safe_attrs, (list, set, tuple)
        ), "safe_attrs must be list\\tuple\\set of strings or unicode"

        if safe_attrs:
            str_types_safe_attrs = [isinstance(attr, str_types) for attr in safe_attrs]

            assert all(
                str_types_safe_attrs
            ), "safe_attrs must be list\\tuple\\set of strings or unicode"
        self.safe_attrs = set(safe_attrs)

        # Next, load our local data file into memory (browsers.json)
        self.data_browsers = load()

    def __getitem__(self, attr):
        return self.__getattr__(attr)

    def __getattr__(self, attr):
        if attr in self.safe_attrs:
            return super(UserAgent, self).__getattr__(attr)

        try:
            # Handle input value
            for value, replacement in settings.REPLACEMENTS.items():
                attr = attr.replace(value, replacement)
            attr = attr.lower()
            attr = settings.SHORTCUTS.get(attr, attr)

            if attr == "random":
                # Filter the browser list based on the browsers array using lambda
                # And based on OS list
                # And percentage is bigger then min percentage
                # And convert the iterator back to a list
                filtered_browsers = list(
                    filter(
                        lambda x: x["browser"] in self.browsers
                        and x["os"] in self.os
                        and x["percent"] >= self.min_percentage,
                        self.data_browsers,
                    )
                )
            else:
                # Or when random isn't select, we filter the browsers array based on the 'attr' using lamba
                # And based on OS list
                # And percentage is bigger then min percentage
                # And convert the iterator back to a list
                filtered_browsers = list(
                    filter(
                        lambda x: x["browser"] == attr
                        and x["os"] in self.os
                        and x["percent"] >= self.min_percentage,
                        self.data_browsers,
                    )
                )

            # Pick a random browser user-agent from the filtered browsers
            # And return the useragent string.
            return random.choice(filtered_browsers).get("useragent")  # noqa: S311
        except (KeyError, IndexError):
            if self.fallback is None:
                raise FakeUserAgentError(
                    f"Error occurred during getting browser: {attr}"
                )  # noqa
            else:
                logger.warning(
                    f"Error occurred during getting browser: {attr}, "
                    "but was suppressed with fallback.",
                )

                return self.fallback

    @property
    def chrome(self):
        return self.__getattr__("chrome")

    @property
    def googlechrome(self):
        return self.chrome

    @property
    def edge(self):
        return self.__getattr__("edge")

    @property
    def firefox(self):
        return self.__getattr__("firefox")

    @property
    def ff(self):
        return self.firefox

    @property
    def safari(self):
        return self.__getattr__("safari")

    @property
    def random(self):
        return self.__getattr__("random")


# common alias
UserAgent = FakeUserAgent
