"""Quikr - Development, made quikr."""

import os


def clr():
    """Clear terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def repeat(text):
    """Infinitely repeats specified text."""
    while True:
        print(text)
