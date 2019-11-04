"""Quikr - Development made quikr."""

# =========================== Required Modules ===========================
import platform
# ========================================================================


# ============================== Exceptions ==============================
class InvalidInputError(Exception):
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
    if times.casefold() == "inf":
        while True:
            print(text)
    elif isinstance(times, int) is True:
        for x in range(0, times):
            print(text)
    else:
        raise InvalidInputError("Second argument "
                                "must be 'inf' or an integer.")
# ========================================================================
