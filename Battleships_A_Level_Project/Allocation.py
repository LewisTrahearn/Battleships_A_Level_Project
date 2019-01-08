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
from random import randint

class Allocation(object):
    """description of class"""

    def __init__(self):

        #CONSTANTS 
        self._VERTICAL = 0
        self._HORIZONTAL = 1

        self.SQUARE_HIT = 'K'
        self.SQUARE_MISS = 'M'

        self.BATTLESHIP_SIZE = 4
        self.CARRIER_SIZE = 5
        self.CRUISER_SIZE = 3
        self.SUBMARINE_SIZE = 4
        self.DESTROYER_SIZE = 2

        self.BATTLESHIP_NAME = 'B'
        self.CARRIER_NAME = 'C'
        self.CRUISER_NAME = 'R'
        self.SUBMARINE_NAME = 'S'
        self.DESTROYER_NAME = 'D'

        self.BOARD_WIDTH = 14
        self.BOARD_HEIGHT = 12;

        self.BLACK = (  0,   0,   0)
        self.WHITE = (255, 255, 255)
        self.BLUE =  (  0,   0, 255)
        self.GREEN = (  0, 255,   0)
        self.RED =   (255,   0,   0)
        self.YELLOW = (250,   167,   74)
        self.PURPLE = (242,   102,   230)
        self.OTHER = (240,204,7)

        #############################

        self._pixels_per_column = 50

        self._board = [['_' for x in range(self.BOARD_WIDTH)] for y in range(self.BOARD_HEIGHT)] 

        self._facade = Facade.facade_layer()

        self._allocate_board(self._board)

    def _allocate_board(self,board): 
        self._clear_board(board)
        self._allocate_ship(board, self.BATTLESHIP_SIZE, self.BATTLESHIP_NAME)
        self._allocate_ship(board, self.CARRIER_SIZE, self.CARRIER_NAME)
        self._allocate_ship(board, self.CRUISER_SIZE, self.CRUISER_NAME)
        self._allocate_ship(board, self.SUBMARINE_SIZE, self.SUBMARINE_NAME)
        self._allocate_ship(board, self.DESTROYER_SIZE, self.DESTROYER_NAME)


    def show_allocation(self, screen):
        
        for row in range(self.BOARD_HEIGHT):
            for col in range(self.BOARD_WIDTH):
                if self._board[row][col] != '_':
                    self._display_at_square(screen,self._board[row][col], row, col)

    def _display_at_square(self,screen,s, row, col):

        x = (300 + (col * self._pixels_per_column)) 
        y = (225 + (row * self._pixels_per_column)) 

        

        if s == self.BATTLESHIP_NAME:
            self._facade.DrawStringArchivoNarrow(screen,s, x, y,self.WHITE, False )
        elif s == self.CARRIER_NAME:
            self._facade.DrawStringArchivoNarrow(screen,s, x, y,self.OTHER, False )
        elif s == self.SUBMARINE_NAME:
            self._facade.DrawStringArchivoNarrow(screen,s, x, y,self.PURPLE, False )
        elif s == self.CRUISER_NAME:
            self._facade.DrawStringArchivoNarrow(screen,s, x, y,self.GREEN, False )
        elif s == self.DESTROYER_NAME:
            self._facade.DrawStringArchivoNarrow(screen,s, x, y,self.YELLOW, False )
        elif s == self.SQUARE_HIT:
            x = (290 + (col * self._pixels_per_column)) 
            y = (212 + (row * self._pixels_per_column)) 
          #  screen.blit(self.hitImage, (x,y))
        elif s == self.SQUARE_MISS:
            x = (290 + (col * self._pixels_per_column)) 
            y = (212 + (row * self._pixels_per_column)) 
          #  screen.blit(self.missImage, (x,y))
        else:
            self.DrawStringArchivoNarrow(screen,s, x, y,self.WHITE, False )


    def _clear_board(self, board):
        for height in range(self.BOARD_HEIGHT):
            for width in range(self.BOARD_WIDTH):
                board[height][width] = '_'

    def _allocate_ship(self,board, ship_size, ship_name):
        
        while True:
            # identify a starting place across the board for a ship
            place_x = randint(0, 13)
            # if the starting place + the ships size >= the board width then re-generate another random number
            # i.e. start again in the loop
            if place_x+ship_size >= 13:
                continue

            # identify a starting place down the board for a ship
            place_y = randint(0, 11)

            # if the starting place + the ships size >= the board width then re-generate another random number
            # i.e. start again in the loop
            if place_y+ship_size >= 11:
                continue

            v_or_h = randint(0, 1) # 0 = vertical 1= horizontal

            does_ship_collide = False

            if v_or_h == self._VERTICAL:
                for i in range(ship_size):
                    if board[place_y+i][place_x] != '_':
                        does_ship_collide = True
                        break
                
                if does_ship_collide == True:
                    continue # go to the top of while loop and find another place

                for i in range(ship_size):
                    board[place_y+i][place_x] = ship_name
            else: # horizontal
                for i in range(ship_size):
                    if board[place_y][place_x+i] != '_':
                        does_ship_collide = True
                        break
                if does_ship_collide == True:
                    continue # go to the top of while loop and find another place

                for i in range(ship_size):
                    board[place_y][place_x+i] = ship_name
            break
