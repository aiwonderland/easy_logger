# Configuration Guide

This guide covers all configuration options available in EasyLogger.

## Basic Configuration

### Log Levels

EasyLogger supports five log levels (from lowest to highest severity):

| Level | Description | Console Color |
|-------|-------------|---------------|
| DEBUG | Detailed diagnostic information | Cyan |
| INFO | General informational messages | Green |
| WARNING | Warning messages for potentially harmful situations | Yellow |
| ERROR | Error messages for serious problems | Red |
| CRITICAL | Critical messages for very serious errors | Purple |

```python
from easy_logger import EasyLogger

# Set log level to DEBUG (shows all messages)
logger = EasyLogger(level="DEBUG")

# Set log level to ERROR (only shows ERROR and CRITICAL)
logger = EasyLogger(level="ERROR")
```

### Log Directory

By default, logs are saved to `./logs/` relative to your current working directory.

```python
from easy_logger import EasyLogger
from pathlib import Path

# Use default directory (./logs/)
logger = EasyLogger()

# Use custom directory
logger = EasyLogger(log_dir=Path("/var/log/myapp"))

# Use relative path
logger = EasyLogger(log_dir=Path("../logs"))
```

### Logger Names

Logger names help identify different parts of your application:

```python
from easy_logger import EasyLogger

# Default name
logger = EasyLogger()  # name="easy_logger"

# Custom names for different modules
api_logger = EasyLogger(name="api")
db_logger = EasyLogger(name="database")
auth_logger = EasyLogger(name="auth")
```

**Note**: Multiple `EasyLogger` instances with the same name share the same underlying Python logger. The last configuration wins.

## Log Rotation Configuration

Log rotation prevents log files from growing indefinitely and consuming disk space.

### max_bytes

Controls when log files are rotated based on size.

```python
from easy_logger import EasyLogger

# Default: 10MB
logger = EasyLogger()

# 5MB rotation
logger = EasyLogger(max_bytes=5 * 1024 * 1024)

# 50MB rotation
logger = EasyLogger(max_bytes=50 * 1024 * 1024)

# 1GB rotation
logger = EasyLogger(max_bytes=1024 * 1024 * 1024)
```

### backup_count

Controls how many backup log files to keep.

```python
from easy_logger import EasyLogger

# Default: Keep 5 backups
logger = EasyLogger()

# Keep only 2 backups
logger = EasyLogger(backup_count=2)

# Keep 10 backups
logger = EasyLogger(backup_count=10)

# Keep all backups (not recommended)
logger = EasyLogger(backup_count=0)
```

### How Rotation Works

1. Logs are written to `YYYYMMDD_log.txt` (e.g., `20260206_log.txt`)
2. When the file reaches `max_bytes`, it's renamed to `20260206_log.txt.1`
3. A new `20260206_log.txt` is created
4. On the next rotation, `.1` becomes `.2`, and a new `.1` is created
5. When `backup_count` is reached, the oldest backup is deleted

Example with `backup_count=3`:
```
20260206_log.txt      # Current log file
20260206_log.txt.1    # Most recent backup
20260206_log.txt.2    # Second backup
20260206_log.txt.3    # Oldest backup (will be deleted on next rotation)
```

## Color Configuration

### Disabling Colors

```python
from easy_logger import EasyLogger

# Disable colored output
logger = EasyLogger(enable_colors=False)
```

Colors are automatically disabled if:
- The terminal doesn't support colors
- Output is redirected to a file
- Running in a non-TTY environment

### Color Scheme

The default color scheme is:

- **DEBUG**: Cyan (`\033[0;36m`)
- **INFO**: Green (`\033[0;32m`)
- **WARNING**: Yellow (`\033[0;33m`)
- **ERROR**: Red (`\033[0;31m`)
- **CRITICAL**: Purple (`\033[0;35m`)

Colors only apply to console output. File logs are never colored.

## Complete Configuration Example

```python
from easy_logger import EasyLogger
from pathlib import Path

logger = EasyLogger(
    name="myapp",                      # Logger name
    level="DEBUG",                     # Show all messages
    log_dir=Path("/var/log/myapp"),   # Custom log directory
    enable_colors=True,                # Enable colored output
    max_bytes=20 * 1024 * 1024,       # 20MB per file
    backup_count=7                     # Keep 7 backups
)
```

## Best Practices

### Development vs Production

```python
import os
from easy_logger import EasyLogger

# Development: verbose logging, colors enabled
if os.getenv("ENV") == "development":
    logger = EasyLogger(
        level="DEBUG",
        enable_colors=True,
        max_bytes=5 * 1024 * 1024,
        backup_count=2
    )
# Production: less verbose, larger files, more backups
else:
    logger = EasyLogger(
        level="INFO",
        enable_colors=False,
        max_bytes=50 * 1024 * 1024,
        backup_count=10
    )
```

### Disk Space Management

Choose `max_bytes` and `backup_count` based on your disk space:

```python
# Low disk space: smaller files, fewer backups
logger = EasyLogger(max_bytes=1 * 1024 * 1024, backup_count=2)  # ~3MB total

# Moderate disk space: default settings
logger = EasyLogger()  # ~60MB total (10MB × 6 files)

# High disk space: larger files, more backups
logger = EasyLogger(max_bytes=100 * 1024 * 1024, backup_count=20)  # ~2.1GB total
```

### Multiple Loggers

```python
from easy_logger import EasyLogger

# Separate loggers for different components
api_logger = EasyLogger(name="api", level="INFO")
db_logger = EasyLogger(name="db", level="DEBUG")
cache_logger = EasyLogger(name="cache", level="WARNING")
```