import json
import sys

# We need files() from Python 3.10 or higher
if sys.version_info >= (3, 10):
    import importlib.resources as ilr
else:
    import importlib_resources as ilr

from fake_useragent.log import logger

# Fallback method for retrieving data file
try:
    from pkg_resources import resource_filename
except ImportError:
    pass

str_types = (str,)


# Load all lines from browser.json file
# Returns array of objects
def load():
    data = []
    try:
        json_lines = (
            ilr.files("fake_useragent.data").joinpath("browsers.json").read_text()
        )
        for line in json_lines.splitlines():
            data.append(json.loads(line))
        ret = data
    except Exception as exc:
        # Empty data just to be sure
        data = []
        logger.warning(
            "Unable to find local data/json file or could not parse the contents using importlib-resources. Try pkg-resource next.",
            exc_info=exc,
        )
        try:
            with open(
                resource_filename("fake_useragent", "data/browsers.json")
            ) as file:
                json_lines = file.read()
                for line in json_lines.splitlines():
                    data.append(json.loads(line))
            ret = data
        except Exception as exc2:
            # Empty data just to be sure
            data = []
            logger.warning(
                "Could not find local data/json file or could not parse the contents using pkg-resource.",
                exc_info=exc2,
            )

    if not ret:
        raise FakeUserAgentError("Data list is empty", ret)

    if not isinstance(ret, list):
        raise FakeUserAgentError("Data is not a list ", ret)
    return ret


from fake_useragent import settings  # noqa # isort:skip
from fake_useragent.errors import FakeUserAgentError  # noqa # isort:skip
