"""
Module Name:
    Main.py

Functions/Methods:
    None

Class:
    None

Imports:
    battleships_game - the main control class for the entire game.

Purpose:
    The purpose of this module is as an entry point to the whole program.
    It will instantiate the main game class, which will control and call
    other objects as required.
    
Author:
    Lewis Trahearn

"""

import battleships_game as battleships_control_class

class runme():
    def __init__(self):
        game = battleships_control_class.BattleshipsGame()
        game.play_game()



if __name__ == "__main__":
    runme()