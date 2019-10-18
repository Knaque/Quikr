"""Quikr - Development made quikr."""

import os
import platform


class InvalidInputError(Exception):
    """Throw error if function input is invalid."""


python_version = str(platform.python_version())


def clr():
    """Clear terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def repeat(text, times="inf"):
    """Repeats specified text a specified amount."""
    if times == "inf":
        while True:
            print(text)
    elif isinstance(times, int) is True:
        for x in range(0, times):
            print(text)
    else:
        raise InvalidInputError("Second argument "
                                "must be 'inf' or an integer.")
