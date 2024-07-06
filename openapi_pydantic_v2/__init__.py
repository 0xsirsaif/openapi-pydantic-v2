__version__ = "0.1.1"

import logging

from .v3 import *

logging.getLogger(__name__).addHandler(logging.NullHandler())
