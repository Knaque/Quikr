"""Quikr - Development, made quikr."""

import os


def clr():
    """Clear terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def repeat(text):
    """Infinitely repeats specified text."""
    while True:
        print(text)


def p(text):
    """Just shorter print."""
    print(text)


def f(num):
    """Just shorter "float()"."""
    float(num)


try:
    a = f(input("Type in\n>>> "))
except ValueError:
    p("bad")
