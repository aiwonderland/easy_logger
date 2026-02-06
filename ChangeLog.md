# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- **BREAKING**: `get_log_filename` and `ensure_log_dir` are now private functions (renamed to `_get_log_filename` and `_ensure_log_dir`). These were internal implementation details and should not have been part of the public API.

### Fixed
- Log files now use rotation to prevent unlimited growth and memory consumption. Added `max_bytes` (default 10MB) and `backup_count` (default 5) parameters to `EasyLogger` to control log rotation behavior. Fixes #1.
