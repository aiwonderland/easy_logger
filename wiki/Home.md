# EasyLogger Wiki

Welcome to the EasyLogger documentation! EasyLogger is a simplified Python logging library with colored console output and automatic log rotation.

## Quick Links

- [API Reference](API-Reference)
- [Configuration Options](Configuration)
- [Migration Guide](Migration-Guide)

## Quick Start

### Installation

```bash
pip install easy-logger
```

### Basic Usage

```python
from easy_logger import EasyLogger

# Create a logger instance
logger = EasyLogger()

# Log messages at different levels
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

### Features

- **Colored Console Output**: Different log levels are displayed in different colors for better readability
- **Automatic File Logging**: Logs are automatically saved to files with date-based naming
- **Log Rotation**: Prevents log files from growing indefinitely (configurable)
- **Simple API**: Easy-to-use interface with sensible defaults
- **Customizable**: Configure log levels, directories, colors, and rotation settings

## What's New in v0.2.0

- **Log Rotation**: Added automatic log rotation to prevent unlimited file growth
- **New Parameters**: `max_bytes` and `backup_count` for controlling log rotation
- **API Cleanup**: Internal utility functions are now properly marked as private

See the [Migration Guide](Migration-Guide) for details on upgrading from v0.1.x.

## Support

- [GitHub Issues](https://github.com/aiwonderland/easy_logger/issues)
- [Changelog](https://github.com/aiwonderland/easy_logger/blob/main/ChangeLog.md)