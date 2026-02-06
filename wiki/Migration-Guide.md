# Migration Guide

## Migrating from v0.1.x to v0.2.0

Version 0.2.0 introduces log rotation and cleans up the public API. This guide will help you upgrade.

### Breaking Changes

#### Removed Public Functions

The following functions are no longer part of the public API:

- `get_log_filename()` → Now private: `_get_log_filename()`
- `ensure_log_dir()` → Now private: `_ensure_log_dir()`

**Impact**: If you were importing these functions directly, you'll need to update your code.

**Before (v0.1.x)**:
```python
from easy_logger import EasyLogger, get_log_filename, ensure_log_dir

# This will break in v0.2.0
filename = get_log_filename()
log_dir = ensure_log_dir()
```

**After (v0.2.0)**:
```python
from easy_logger import EasyLogger

# These functions are now internal implementation details
# If you need custom log filenames or directories, use the EasyLogger parameters:
logger = EasyLogger(log_dir=Path("/custom/path"))
```

**Who is affected**: Only users who were directly importing and using these utility functions. If you were only using `EasyLogger`, no changes are needed.

### New Features

#### Log Rotation

Version 0.2.0 adds automatic log rotation to prevent log files from growing indefinitely.

**Default behavior**:
- Log files rotate when they reach 10MB
- 5 backup files are kept
- Older backups are automatically deleted

**No action required**: Log rotation is enabled by default with sensible defaults.

**Customization** (optional):
```python
from easy_logger import EasyLogger

# Customize rotation settings
logger = EasyLogger(
    max_bytes=20 * 1024 * 1024,  # 20MB per file
    backup_count=10               # Keep 10 backups
)
```

#### New Parameters

Two new optional parameters have been added to `EasyLogger`:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `max_bytes` | int | 10485760 (10MB) | Maximum log file size before rotation |
| `backup_count` | int | 5 | Number of backup files to keep |

### Migration Checklist

- [ ] Check if you're importing `get_log_filename` or `ensure_log_dir`
- [ ] If yes, remove these imports and use `EasyLogger` parameters instead
- [ ] Update your `requirements.txt` or `pyproject.toml` to `easy-logger>=0.2.0`
- [ ] Test your application to ensure logging still works
- [ ] (Optional) Configure log rotation settings if defaults don't suit your needs

### Example Migration

#### Before (v0.1.x)

```python
from easy_logger import EasyLogger, ensure_log_dir
from pathlib import Path

# Manually ensure log directory exists
log_dir = ensure_log_dir(Path("/var/log/myapp"))

# Create logger
logger = EasyLogger(log_dir=log_dir)
logger.info("Application started")
```

#### After (v0.2.0)

```python
from easy_logger import EasyLogger
from pathlib import Path

# EasyLogger handles directory creation automatically
logger = EasyLogger(
    log_dir=Path("/var/log/myapp"),
    max_bytes=10 * 1024 * 1024,  # Optional: configure rotation
    backup_count=5                # Optional: configure backups
)
logger.info("Application started")
```

### Compatibility

- **Python Version**: No changes (still supports Python 3.7+)
- **Dependencies**: No new dependencies added
- **Backward Compatibility**: Breaking changes only affect direct usage of utility functions

### Troubleshooting

#### ImportError: cannot import name 'get_log_filename'

**Problem**: You're trying to import a function that's no longer public.

**Solution**: Remove the import. If you need custom log filenames, use the `log_dir` parameter:

```python
# Instead of:
# from easy_logger import get_log_filename
# filename = get_log_filename()

# Use:
from easy_logger import EasyLogger
logger = EasyLogger(log_dir=Path("/custom/path"))
```

#### ImportError: cannot import name 'ensure_log_dir'

**Problem**: You're trying to import a function that's no longer public.

**Solution**: Remove the import. `EasyLogger` automatically creates the log directory:

```python
# Instead of:
# from easy_logger import ensure_log_dir
# ensure_log_dir(Path("/var/log/myapp"))

# Use:
from easy_logger import EasyLogger
logger = EasyLogger(log_dir=Path("/var/log/myapp"))
```

#### Log files are being rotated unexpectedly

**Problem**: Log files are rotating more frequently than expected.

**Solution**: Increase the `max_bytes` parameter:

```python
logger = EasyLogger(
    max_bytes=50 * 1024 * 1024  # 50MB instead of default 10MB
)
```

#### Too many backup files

**Problem**: Too many backup log files are accumulating.

**Solution**: Decrease the `backup_count` parameter:

```python
logger = EasyLogger(
    backup_count=2  # Keep only 2 backups instead of default 5
)
```

### Getting Help

If you encounter issues during migration:

1. Check the [API Reference](API-Reference) for updated documentation
2. Review the [Configuration Guide](Configuration) for rotation settings
3. Open an issue on [GitHub](https://github.com/aiwonderland/easy_logger/issues)

### Changelog

For a complete list of changes, see the [Changelog](https://github.com/aiwonderland/easy_logger/blob/main/ChangeLog.md).