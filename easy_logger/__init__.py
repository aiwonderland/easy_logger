# easy_logger/__init__.py
"""
EasyLogger - A simplified Python logging library with colored console output.

This package provides an easy-to-use logging interface with automatic
file logging and colored console output.
"""

from .core import EasyLogger
from .utils import get_log_filename, ensure_log_dir

__version__ = "1.0.0"
__author__ = "aiwonderland"
__all__ = [
    "EasyLogger",
    "get_log_filename",
    "ensure_log_dir",
]