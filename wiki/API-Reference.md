# API Reference

## EasyLogger Class

The main class for creating and managing loggers.

### Constructor

```python
EasyLogger(
    name: str = "easy_logger",
    level: str = "INFO",
    log_dir: Optional[Path] = None,
    enable_colors: bool = True,
    max_bytes: int = 10 * 1024 * 1024,
    backup_count: int = 5
)
```

#### Parameters

- **name** (str, optional): Logger name. Default: `"easy_logger"`
  - Used to identify the logger instance
  - Multiple loggers with the same name share the same underlying Python logger

- **level** (str, optional): Log level. Default: `"INFO"`
  - Valid values: `"DEBUG"`, `"INFO"`, `"WARNING"`, `"ERROR"`, `"CRITICAL"`
  - Case-insensitive

- **log_dir** (Path, optional): Custom log directory. Default: `None`
  - If `None`, logs are saved to `./logs/`
  - Directory will be created if it doesn't exist

- **enable_colors** (bool, optional): Enable colored console output. Default: `True`
  - Colors are automatically disabled if the terminal doesn't support them
  - File logs are never colored

- **max_bytes** (int, optional): Maximum log file size before rotation. Default: `10485760` (10MB)
  - When a log file reaches this size, it's rotated
  - Set to a larger value for more logs per file

- **backup_count** (int, optional): Number of backup log files to keep. Default: `5`
  - Older backup files are automatically deleted
  - Set to `0` to keep all backups (not recommended)

### Methods

#### debug(msg, *args, **kwargs)

Log a debug message.

```python
logger.debug("Debug message")
logger.debug("User %s logged in", username)
```

#### info(msg, *args, **kwargs)

Log an info message.

```python
logger.info("Application started")
logger.info("Processing %d items", count)
```

#### warning(msg, *args, **kwargs)

Log a warning message.

```python
logger.warning("Disk space low")
logger.warning("Deprecated function called: %s", func_name)
```

#### error(msg, *args, **kwargs)

Log an error message.

```python
logger.error("Failed to connect to database")
logger.error("Error processing file: %s", filename)
```

#### critical(msg, *args, **kwargs)

Log a critical message.

```python
logger.critical("System failure")
logger.critical("Out of memory")
```

## Examples

### Basic Logging

```python
from easy_logger import EasyLogger

logger = EasyLogger()
logger.info("Application started")
logger.error("An error occurred")
```

### Custom Configuration

```python
from easy_logger import EasyLogger
from pathlib import Path

logger = EasyLogger(
    name="myapp",
    level="DEBUG",
    log_dir=Path("/var/log/myapp"),
    enable_colors=True,
    max_bytes=5 * 1024 * 1024,  # 5MB
    backup_count=3
)
```

### Multiple Loggers

```python
from easy_logger import EasyLogger

# Create separate loggers for different modules
api_logger = EasyLogger(name="api", level="INFO")
db_logger = EasyLogger(name="database", level="DEBUG")

api_logger.info("API request received")
db_logger.debug("Query executed")
```

## Log File Format

Log files are saved with the following format:

- **Filename**: `YYYYMMDD_log.txt` (e.g., `20260206_log.txt`)
- **Location**: `./logs/` by default
- **Rotation**: When file reaches `max_bytes`, it's renamed to `.1`, `.2`, etc.
- **Format**: `YYYY-MM-DD HH:MM:SS - logger_name - LEVEL - message`

Example log entry:
```
2026-02-06 14:30:45 - easy_logger - INFO - Application started
```