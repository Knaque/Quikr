"""Quikr - Development made quikr."""

# =========================== Required Modules ===========================
import platform
# ========================================================================


# ============================== Exceptions ==============================
class InvalidArgumentError(Exception):
    """Throw error if input is invalid."""
class MissingDependencyError(Exception):
    """Throw error if a dependency is missing."""
# ========================================================================


# ============================== Variables ===============================
# NOTE: Can someone work out a way of doing these so that platform is only
# imported if the variables are called? Using this in a function and calling
# as a variable [ex. print(q.py_version())] adds a "None" line for some reason.

# Variable for current Python version
py_version = str(platform.python_version())

# Variable for current OS
os = str(platform.system())
# ========================================================================


# ============================== Functions ===============================
def clear():
    """Clear terminal."""
    import os  # Will be imported if it hasn't been already
    os.system('cls' if os.name == 'nt' else 'clear')


def repeat(text, times="inf"):
    """Repeats specified text x times."""
    if isinstance(times, int) is True:
        for x in range(0, times):
            print(text)
    elif times.casefold() == "inf":
        while True:
            print(text)
    else:
        raise InvalidArgumentError("Second argument must "
                                   "be 'inf' or an integer.")


def rainbow(str):
    '''Takes a string as input and returns the string in rainbow form. Requires Colorama.'''
    try: from colorama import init, Fore, Style; init()  # Will be imported if it hasn't been already; Return error message if not installed.
    except ModuleNotFoundError: raise MissingDependencyError("rainbow() requires Colorama to work: pip install colorama")
    from itertools import cycle  # Will be imported if it hasn't been already

    colorful = Style.BRIGHT

    for char, col in zip(str, cycle([Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA])):
        colorful = colorful + col + char

    return colorful + Style.RESET_ALL
# ========================================================================
