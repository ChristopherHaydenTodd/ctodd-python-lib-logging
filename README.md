# Christopher H. Todd's Python Library For Configuring Logging

The ctodd-python-lib-logging project is responsible for configuring the logging for python scripts. Will set up the level, format of the messages, and the stream.

## Table of Contents

- [Dependencies](#dependencies)
- [Libraries](#libraries)
- [Example Scripts](#example-scripts)
- [Notes](#notes)
- [TODO](#todo)

## Dependencies

### Python Packages

- N/A

## Libraries

### [loggers.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-logging/blob/master/logging_helpers/loggers.py)

Library for getting loggers of specific configurations in Python. This will utilize Pythons built-in logging library and will return an instance of logging that can be implemented in any code that already implements the logging class.

Functions:

```
def get_stdout_logging(
    log_level=logging.INFO,
    log_msg_fmt="%(asctime)s.%(msecs)03d %(levelname)s %(message)s",
    log_date_fmt="%a, %d %b %Y %H:%M:%S",
    log_prefix=None,
):
    """
    Purpose:
        Get Logger to standard out.
    Args:
        log_level (log level from logging): Minimum level for messages to log
        log_msg_fmt (String): Mesage format for all logs with variable
            substitution for known logging options
        log_date_fmt (Stringg): Dateformat to append to message
        log_prefix (String): prefix to append to message
    Return:
        logging (Python logging object): Configured logging object
    Examples:
        >>> logging = get_stdout_logging()
        or
        >>> logging =\
            get_stdout_logging(
                log_level=logging.DEBUG,
                log_prefix='[test_script]: '',
            )
    """
```

```
def get_file_logger(
    log_file=None,
    log_filemode="a",
    log_level=logging.INFO,
    log_msg_fmt="%(asctime)s %(levelname)s %(message)s",
    log_date_fmt="%a, %d %b %Y %H:%M:%S",
    log_prefix=None,
):
    """
    Purpose:
        Get Logger to file
    Args:
        log_level (log level from logging): Minimum level for messages to log
        log_msg_fmt (String): Mesage format for all logs with variable
            substitution for known logging options
        log_date_fmt (Stringg): Dateformat to append to message
        log_prefix (String): prefix to append to message
    Return:
        logging (Python logging object): Configured logging object
    Examples:
        >>> logging = get_file_logger()
        or
        >>> logging =\
            get_file_logger(
                log_level=logging.ERROR,
                prefix='[test_script]: '',
                log_file='./script_im_writing.log'
            )
    """
```

```
def clear_log_handlers():
    """
    Purpose:
        Remove previous log handlers and configurations. This
        will ensure that any new logging that is configured
        will take precedence, as logging is first setting
        is not overwritten.
    Args:
        N/A
    Return:
        N/A
    """
```

## Example Scripts

Example executable Python scripts/modules for testing and interacting with the library. These show example use-cases for the libraries and can be used as templates for developing with the libraries or to use as one-off development efforts.

### [example_stdout_logger.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-logging/blob/master/example_usage/example_stdout_logger.py)

```
Example Logger. Configure to Output to CLI
```

## Notes

 - Relies on f-string notation, which is limited to Python3.6.  A refactor to remove these could allow for development with Python3.0.x through 3.5.x

## TODO

 - Unittest framework in place, but lacking tests
