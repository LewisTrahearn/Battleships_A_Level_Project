"""
Module Name:
    Board.py

Functions/Methods:
    Draw

Class:
    Board


Imports:
    navigate        - common enumeration values shared across all classes on where to go next in the game
    facade_layer    - an abstraction from the pygame module, for certain common functions
    import pygame   - pygame library
    pygame.locals   - this is needed for the Rect definition

Purpose:
    The purpose of this class is to Draw the grid and axes of the gameboard
  
    
Author:
    Lewis Trahearn

"""

from random import randint
import pygame
from pygame.locals import *

from navigate import Navigate
import facade_layer as Facade
import DataAcessLayer as DataAccessLayer



class Board(object):
    """description of class"""
    def __init__(self, screen):
        #CONSTANTS
        self._WHITE = (255, 255, 255)
        self._RED =   (255,   0,   0)
        self._YELLOW = (250,   167,   74)
        self._BLUE =  (  0,   0, 255)
        self._COORD_COLOR =  (  170,   240, 114)
        self._X_AXIS_RANGE = 14 #  number of squares across
        self._Y_AXIS_RANGE = 12 #  number of squares down

        
        # Class Instance Variables
        self._screen = screen
        self._origin_x = randint(0, 13)
        self._origin_y = randint(0, 12)
        self._pixels_per_column = 50

        self.x_axis_labels = list(range(-20,40)) # create an array prefilled with numbers from -20 to 59
        self.y_axis_labels = list(range(-20,40)) # create an array prefilled with numbers from -20 to 59
        # I know that the 20th Element is a zero i.e. the origin of the coordinate axis

        # These are now the starting points for documenting the axes
        self.x_axis_starting_point = 20 - self._origin_x
        self.y_axis_starting_point = 20 - self._origin_y

        # Create the facade layer so we can draw the labels to screen
        self._facade = Facade.facade_layer()


    def draw(self):
        self._draw_grid()
        self._draw_axes()
    
    def _draw_grid(self):
        x = 290
        y = 212
        counter = 0
        line_width = 4
        for i in range(15):
            pygame.draw.line(self._screen, self._WHITE, (x, 212), (x,811), line_width)
            x = x + 50
         

        for i in range(13):
            pygame.draw.line(self._screen, self._WHITE, (290, y), (988,y), line_width)
            y = y + 50

    def user_coords_to_array_coords(self, ux, uy):

        counter = self.x_axis_starting_point
        for i in range(self._X_AXIS_RANGE):
            if self.x_axis_labels[counter] == ux:
                break
            counter = counter + 1
        
        x = i

        counter = self.y_axis_starting_point
        for i in range(self._Y_AXIS_RANGE):
            if self.y_axis_labels[counter] == uy:
                break
            counter = counter + 1
        
        y = i
        return x,y


    def user_coords_to_screen_coords(self, ux, uy):
        x, y = self.user_coords_to_array_coords( ux, uy)
        x = (x * self._pixels_per_column) + 290
        y = (y * self._pixels_per_column) + 212
        return x,y

    def _draw_axes(self):
        start = 290
        line_width = 4

        ##################################################################################
        # Draw Axes Lines in RED
        ##################################################################################
        x = start + (self._origin_x * self._pixels_per_column)
        y = 212 + (self._origin_y * self._pixels_per_column)
        pygame.draw.line(self._screen, self._RED, (x, 212), (x,811), line_width)
        pygame.draw.line(self._screen, self._RED, (290, y), (988,y), line_width)

        ################################################################################
        # label the X - Axis 
        ################################################################################


        x = start 
        y = 212 + (self._origin_y * self._pixels_per_column)

        counter = self.x_axis_starting_point

        for i in range(self._X_AXIS_RANGE):
            if self.x_axis_labels[counter] != 0:
                number = str(self.x_axis_labels[counter] )
                self._facade.DrawStringArchivoNarrow(self._screen,number, x, y,self._RED, False )
            x = x + self._pixels_per_column
            counter = counter + 1

        ################################################################################
        # label the Y - Axis 
        ################################################################################


        x = start + (self._origin_x * self._pixels_per_column) + 10
        y = 212 #+ (self.OriginY * self.PixelsPerColumn) 

        counter = self.y_axis_starting_point

        for i in range(self._Y_AXIS_RANGE):
            number = str(self.y_axis_labels[counter] )
            self._facade.DrawStringArchivoNarrow(self._screen,number, x, y,self._RED, False )
            y = y + self._pixels_per_column
            counter = counter + 1
