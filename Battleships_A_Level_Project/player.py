"""
Module Name:
    player.py

Functions/Methods:
    play

Class:
    player


Imports:
    navigate        - common enumeration values shared across all classes on where to go next in the game
    facade_layer    - an abstraction from the pygame module, for certain common functions
    import pygame   - pygame library
    pygame.locals   - this is needed for the Rect definition

Purpose:
    The purpose of this class is to define a player for the game.
    Within this game you will have a player 1, player 2 and Computer
  
    
Author:
    Lewis Trahearn

"""
import pygame
from pygame.locals import *

from navigate import Navigate
import facade_layer as Facade
import DataAcessLayer as DataAccessLayer




class player(object):
    """description of class"""


