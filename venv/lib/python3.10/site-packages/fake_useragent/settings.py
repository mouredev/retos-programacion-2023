try:
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata

__version__ = metadata.version("fake-useragent")

REPLACEMENTS = {
    " ": "",
    "_": "",
}

OS_REPLACEMENTS = {
    "windows": "win10",
}

SHORTCUTS = {
    "microsoft edge": "edge",
    "google": "chrome",
    "googlechrome": "chrome",
    "ff": "firefox",
}
