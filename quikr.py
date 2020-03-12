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
    """Converts text into a colored rainbow of said text, currently only works in version 2.7."""
    # TODO: TheCrappyCoder, Ensure that this user input is sanitized and make sure that you add a try except statment in case string is not str
    # TODO: TheCrappyCode, make a version of this that works for python versions == or >= 2.7
    if "2.7" in platform.python_version():
        from colorama import Fore
        from itertools import cycle
        nums = [1, 2, 3, 4, 5]  # Since the colorama module doesn't have a few colors commonly found on the rainbow, we are limited to five if you count my Magenta substitute
        colorful = ""
        for char, x in zip(string, cycle(nums)):
            # TODO: TheCrappyCoder, Find a more efficent method for this you buffon, and make this run properly
            if x == 1:
                colorful += Fore.RED + char
            elif x == 2:
                colorful += Fore.YELLOW + char
            elif x == 3:
                colorful += Fore.GREEN + char
            elif x == 4:
                colorful += Fore.BLUE + char
            elif x == 5:
                colorful += Fore.MAGENTA + char
        return colorful
    elif "2.7" not in platform.python_version():
        print("This function only works in Python 2.7, we'll get around to adding a working version for more versions soon.")
        exit()
# ========================================================================
