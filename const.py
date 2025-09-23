import os.path
from dataclasses import dataclass


@dataclass
class ConstPath:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')


@dataclass
class ConstBrowser:
    DEFAULT_BROWSER_VERSION = "128.0"
    DEFAULT_BROWSER_TYPE = "chrome"
