# easy_logger/core.py
import logging
import sys
from pathlib import Path
from typing import Any, Optional
from .utils import get_log_filename, ensure_log_dir

# Define colored output format (make logs more intuitive)
COLORS = {
    "DEBUG": "\033[0;36m",    # Cyan
    "INFO": "\033[0;32m",     # Green
    "WARNING": "\033[0;33m",  # Yellow
    "ERROR": "\033[0;31m",    # Red
    "CRITICAL": "\033[0;35m"  # Purple
}
RESET = "\033[0m"

def _supports_color() -> bool:
    """Check if the terminal supports color output."""
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

class EasyLogger:
    def __init__(
        self,
        name: str = "easy_logger",
        level: str = "INFO",
        log_dir: Optional[Path] = None,
        enable_colors: bool = True
    ):
        """
        Initialize a simplified logger with console and file output.

        Args:
            name: Logger name
            level: Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)
            log_dir: Custom log directory (default: uses ensure_log_dir())
            enable_colors: Enable colored console output (default: True)
        """
        # 1. Create logger instance
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper()))
        self.logger.handlers.clear()  # Avoid duplicate handlers
        self.enable_colors = enable_colors and _supports_color()

        # 2. Define log format
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # 3. Console handler (colored output)
        console_handler = logging.StreamHandler()
        if self.enable_colors:
            console_handler.setFormatter(self._get_color_formatter(formatter))
        else:
            console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # 4. File handler (save to log file)
        log_directory = ensure_log_dir(log_dir) if log_dir else ensure_log_dir()
        log_file = log_directory / get_log_filename()
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def _get_color_formatter(self, base_formatter: logging.Formatter) -> logging.Formatter:
        """
        Create a formatter that adds color codes to log output.

        Args:
            base_formatter: The base formatter to wrap

        Returns:
            A ColorFormatter instance
        """
        class ColorFormatter(logging.Formatter):
            def format(self, record: logging.LogRecord) -> str:
                # Store original values
                original_levelname = record.levelname

                # Add color to different log levels
                if record.levelname in COLORS:
                    color = COLORS[record.levelname]
                    record.levelname = f"{color}{record.levelname}{RESET}"

                # Format the message
                result = base_formatter.format(record)

                # Restore original levelname
                record.levelname = original_levelname

                return result
        return ColorFormatter()

    # Expose logging methods (simplify calls)
    def debug(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Log a debug message."""
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Log an info message."""
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Log a warning message."""
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Log an error message."""
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        """Log a critical message."""
        self.logger.critical(msg, *args, **kwargs)