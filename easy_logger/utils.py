# easy_logger/utils.py
from datetime import datetime
from pathlib import Path
from typing import Union

DEFAULT_LOG_DIR = Path("./logs")

def get_log_filename(date_format: str = "%Y%m%d") -> str:
    """
    Generate a log filename with a date.

    Args:
        date_format: The date format string (default: "%Y%m%d")

    Returns:
        A filename string like "20260206_log.txt"
    """
    today = datetime.now().strftime(date_format)
    return f"{today}_log.txt"

def ensure_log_dir(log_dir: Union[str, Path] = DEFAULT_LOG_DIR) -> Path:
    """
    Ensure the log directory exists; create it if it does not.

    Args:
        log_dir: The directory path (default: "./logs")

    Returns:
        The Path object for the log directory

    Raises:
        OSError: If directory creation fails
    """
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    return log_path