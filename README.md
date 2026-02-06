# EasyLogger Usage Guide

A simplified Python logging library with colored console output and automatic file logging.

## Installation

```python
from easy_logger import EasyLogger
```

## Basic Usage

### Simple Logging

```python
from easy_logger import EasyLogger

# Create a logger with default settings
logger = EasyLogger()

# Log messages at different levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

## Advanced Configuration

### Custom Logger Name and Level

```python
# Create a logger with custom name and log level
logger = EasyLogger(name="my_app", level="DEBUG")
```

**Available log levels:**
- `DEBUG` - Detailed information for debugging
- `INFO` - General informational messages (default)
- `WARNING` - Warning messages
- `ERROR` - Error messages
- `CRITICAL` - Critical error messages

### Custom Log Directory

```python
from pathlib import Path

# Use a custom directory for log files
logger = EasyLogger(log_dir=Path("./custom_logs"))

# Or use a string path
logger = EasyLogger(log_dir="./app_logs")
```

### Disable Colored Output

```python
# Disable colored console output
logger = EasyLogger(enable_colors=False)
```

### Combined Configuration

```python
from pathlib import Path

# Combine multiple options
logger = EasyLogger(
    name="my_app",
    level="WARNING",
    log_dir=Path("./app_logs"),
    enable_colors=True
)
```

## Logging Features

### String Formatting

```python
# Use % formatting
logger.info("User %s logged in", username)
logger.error("Failed to process %s: %s", filename, error_msg)

# Multiple arguments
logger.debug("Processing item %d of %d", current, total)
```

### Exception Logging

```python
# Log exceptions with traceback
try:
    risky_operation()
except Exception as e:
    logger.error("Operation failed", exc_info=True)
```

### Extra Context

```python
# Add extra context to log messages
logger.info("User action", extra={'user_id': 123, 'action': 'login'})
```

## Features

### Automatic Features

- **Colored Console Output**: Automatically detects terminal color support
  - DEBUG: Cyan
  - INFO: Green
  - WARNING: Yellow
  - ERROR: Red
  - CRITICAL: Purple

- **File Logging**: Automatically saves logs to files
  - Default location: `./logs/YYYYMMDD_log.txt`
  - Format: `20260206_log.txt`
  - Encoding: UTF-8

- **Dual Output**: Logs are written to both console and file simultaneously

### Type Safety

The library includes full type hints for better IDE support and type checking:

```python
from easy_logger import EasyLogger
from pathlib import Path

logger: EasyLogger = EasyLogger(
    name="my_app",
    level="INFO",
    log_dir=Path("./logs"),
    enable_colors=True
)
```

## Examples

### Web Application Logging

```python
from easy_logger import EasyLogger

logger = EasyLogger(name="web_app", level="INFO")

logger.info("Server started on port 8000")
logger.warning("High memory usage detected: 85%%")
logger.error("Database connection failed", exc_info=True)
```

### Script Logging

```python
from easy_logger import EasyLogger
from pathlib import Path

logger = EasyLogger(
    name="data_processor",
    level="DEBUG",
    log_dir=Path("./script_logs")
)

logger.debug("Starting data processing")
logger.info("Processed %d records", record_count)
logger.warning("Skipped %d invalid records", invalid_count)
```

### Production Logging

```python
from easy_logger import EasyLogger

# Production: WARNING level, no colors for log aggregation
logger = EasyLogger(
    name="production_app",
    level="WARNING",
    enable_colors=False
)

logger.warning("API rate limit approaching")
logger.error("Payment processing failed for order %s", order_id)
logger.critical("Database connection pool exhausted")
```

## Log File Management

Log files are automatically created with the current date:
- Format: `YYYYMMDD_log.txt`
- Example: `20260206_log.txt`
- Location: `./logs/` (or custom directory)

Each day creates a new log file, making it easy to manage and archive logs.

## Notes

- The logger automatically creates the log directory if it doesn't exist
- Console colors are automatically disabled when output is redirected or piped
- File logs never contain color codes, only plain text
- Multiple logger instances can coexist with different configurations
