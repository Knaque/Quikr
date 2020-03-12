"""Quikr - Development made quikr."""

# =========================== Required Modules ===========================
import platform
# ========================================================================


# ============================== Exceptions ==============================
class InvalidArgumentError(Exception):
    """Throw error if input is invalid."""
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


def rainbow(string):
    # TODO: TheCrappyCoder, Ensure that this user input is sanitized and make sure that you add a try except statment in case string is not str
    from colorama import Fore
    from itertools import cycle
    nums = [ i for i in [1, 2, 3, 4, 5, 6, 7, 8]]
    for char, x in zip(string, nums):
        # TODO: TheCrappyCoder, Find a more efficent method for this you buffon
        colorful += Fore.Red, char if x == 1
        colorful += Fore.Orange, char if x == 2
        colorful += Fore.Yellow, char if x == 3
        colorful += Fore.Green, char if x == 4
        colorful += Fore.Blue, char if x == 5
        colorful += Fore.Indigo, char if x == 6
        colorful += Fore.Violet, char if x == 7
    return colorful
# ========================================================================
