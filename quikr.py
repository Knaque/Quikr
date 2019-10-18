"""Quikr - Development made quikr."""

# =========================== Required Modules ===========================
import platform
# ========================================================================


# ============================== Exceptions ==============================
class InvalidInputError(Exception):
    """Throw error if input is invalid."""
# ========================================================================


# ============================== Variables ===============================
# Variable for calling current Python version
# NOTE: Can someone work out a way of doing this so that platform is only
# imported if the variable is called? Using this in a function and calling as a
# var adds a "None" line for some reason. ~Reilly
py_version = str(platform.python_version())
# ========================================================================


# ============================== Functions ===============================
def clear():
    """Clear terminal."""
    import os  # Will be imported if it hasn't been already
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
# ========================================================================
