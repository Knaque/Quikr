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
    '''Converts text (str) into a colored rainbow of said text, tested to work on versions 2.7+.'''
    # TODO: TheCrappyCoder, Ensure that this user input is sanitized and make sure that you add a try except statment in case string is not str
    from itertools import cycle
    nums = [1, 2, 3, 4, 5]
    colorful = ""
    for char, x in zip(string, cycle(nums)):
        # TODO: TheCrappyCoder, Find a more efficent method for this, you buffon
        if x == 1:
            colorful += "\033[0;31m" + char  # Red
        elif x == 2:
            colorful +=  "\033[1;33m" + char  # Yellow (we can't go in sequential order since the ANSI standard doesn't have an orange)
        elif x == 3:
            colorful += "\033[0;32m" + char  # Green
        elif x == 4:
            colorful += "\033[0;34m" + char  # Blue
        elif x == 5:
            colorful += "\033[0;35m" + char  # Purple (No ANSI Indigo or Violet)
    return colorful
# ========================================================================
