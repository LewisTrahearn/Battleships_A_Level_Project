"""
Module Name:
    enum_navigate.py

Functions/Methods:
    none

Class:
    enum_navigate - define a set of standard enums to navigate between the screens.

Imports:
    enum - python 3.7 enumeration type

Purpose:
    define a set of standard enums to navigate between the screens.
    
Author:
    Lewis Trahearn

"""
from enum import Enum

class Navigate(Enum):
    """
    A list of valid enumeration types to be used across
    all classes for navigation between screens.

    """

    SPLASHSCREEN = 1
    REGISTER = 2
    LOGIN = 3
    OPTIONS = 4
    MAIN_GAME = 5
    HIGHSCORES = 6
    QUIT_SPLASHSCREEN = 7
    HELP_SCREEN = 8

