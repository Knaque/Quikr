"""Quikr - Development made quikr."""

import os
import platform


class InvalidInputError(Exception):
    """Throw error if function input is invalid."""


# Variable for calling current Python version
python_version = str(platform.python_version())


def clear():
    """Clear terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def repeat(text, times="inf"):
    """Repeats specified text a specified amount."""
    if times.casefold() == "inf":
        while True:
            print(text)
    elif isinstance(times, int) is True:
        for x in range(0, times):
            print(text)
    else:
        raise InvalidInputError("Second argument "
                                "must be 'inf' or an integer.")
