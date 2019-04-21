#!/usr/bin/env python3
"""
    Purpose:
        Example Logger. Configure to Output to CLI

    Steps:
        -

    function call: python3.6 example_stdout_logger.py
"""

# Python Library Imports
import os
import sys
from argparse import ArgumentParser

# Local Library Imports
BASE_PROJECT_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/../"
sys.path.insert(0, BASE_PROJECT_PATH)
from logging_helpers import loggers


def main():
    """
    Purpose:
        Show Example Execution
    """
    logging.info("Starting The Script to Test Loggers")

    # Stuff would go here

    logging.info("The Script to Test Loggers Complete")


###
# General/Helper Methods
###


def get_options():
    """
    Purpose:
        Parse CLI arguments for script
    Args:
        N/A
    Return:
        N/A
    """

    parser = ArgumentParser(description="Example Standard Out Logger")
    required = parser.add_argument_group('Required Arguments')
    optional = parser.add_argument_group('Optional Arguments')

    # Optional Arguments
    # N/A

    # Required Arguments
    # N/A

    return parser.parse_args()


if __name__ == "__main__":

    try:
        logging = loggers.get_stdout_logging(log_prefix="[example_stdout_logger] ")
        main()
    except Exception as err:
        print(
            "{0} failed due to error: {1}".format(os.path.basename(__file__), err)
        )
        raise err
