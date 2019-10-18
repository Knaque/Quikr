<<<<<<< HEAD
"""Quikr - Development made quikr."""
=======
"""Quikr - Python development, made quikr."""
>>>>>>> 3aa8bf61174b391e6cdaf07ffcfe1757d8c469cf

import os
import platform


class InvalidInputError(Exception):
    """Throw error if function input is invalid."""


# Variable for calling current Python version
python_version = str(platform.python_version())


def clr():
    """Clear terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


<<<<<<< HEAD
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
=======
def repeat(text):
    """Infinitely repeats specified text."""
    while True:
        print(text)


def p(text):
    """Just shorter print()."""
    print(text)


def f(num):
    """Just shorter "float()"."""
    float(num)


def i(num):
    """Just shorter "int()"."""
    int(num)
>>>>>>> 3aa8bf61174b391e6cdaf07ffcfe1757d8c469cf
