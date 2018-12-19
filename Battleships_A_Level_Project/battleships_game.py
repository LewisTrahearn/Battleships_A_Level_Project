


"""
Module Name:
    battleships_game.py

Functions/Methods:
    constructor - default no arguments
    play_game - public method

Class:
    BattleshipsGame - the main control class of the whole game.

Imports:
    enum_navigate - enum class for navigation values

Purpose:
    the main control class of the whole game. It will coordinate
    between all of the screens within the game according to the 
    users input.

Author:
    Lewis Trahearn    

"""


import splashscreen as ss

class BattleshipsGame():
    """
    description:
        the main control class of the whole game. It will coordinate
        between all of the screens within the game according to the 
        users input.
    
    attributes:

    methods:
        __init__(self) - default constructor no parameters required
        playGame(self): - public method and only entry point to the class


    """

    def __init__(self):
        pass

    def play_game(self):
        splash = ss.SplashScreen(0, 0, 1280, 1024)
        where_next = splash.display()