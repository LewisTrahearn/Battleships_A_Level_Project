


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
import DataAcessLayer as DataAccessLayer
import login as LoginScreen
import Register as RegisterScreen 
from navigate import Navigate
import Options as OptionsScreen
import testXML

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
        self._dal = DataAccessLayer.DataAccessLayer()


    def _login(self):
        login = LoginScreen.Login(0, 0, 1280, 1024, self._dal)
        return login.display() 

    def _register(self):
        register = RegisterScreen.Register(0, 0, 1280, 1024, self._dal)
        return register.display()


    def _splashscreen(self):
        splash = ss.SplashScreen(0, 0, 1280, 1024)
        where_next = splash.display()
        return where_next

    def _options(self):
        option = OptionsScreen.Options(0, 0, 1280, 1024, self._dal)
        where_next = option.display()
        return where_next



    def play_game(self):
       
        where_next = Navigate.SPLASHSCREEN

        while True:
            if where_next == Navigate.LOGIN:
                where_next = self._login()

            if where_next == Navigate.SPLASHSCREEN:
                where_next = self._splashscreen()


            if where_next == Navigate.REGISTER:
                where_next = self._register()

            if where_next == Navigate.OPTIONS:
                where_next = self._options()

               



