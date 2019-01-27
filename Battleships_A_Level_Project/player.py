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

import DataAcessLayer as DataAccessLayer
import Board as Board
import Allocation as Allocation
import facade_layer as Facade


class Player(object):
    """description of class"""

    def __init__(self, board, allocation, dal, screen):

        self._board = board
        self._allocation = allocation
        self._dal = dal
        self._screen = screen
        self._facade = Facade.facade_layer()
        
        self._board_width = self._allocation.board_width
        self._board_height = self._allocation.board_height

        self._shot_taken = False
        self._next_player = False
        self._swap_player = False

        self._next_button_coords = Rect(800,975,100,80)


        self._control_x_col = 0 # this keeps track of where we are on the slider control for x and identifies our chosen column
        self._control_y_row = 0 # this keeps track of where we are on the slider control for y and identifies our chosen row
        self._display_x = 0
        self._display_y = 0

        self._ready = True  # this determines whether we are ready for the next input

        # CONSTANTS FOR BUTTONS
        self.SLIDER_X_MINUS     = Rect(417,860,21,30)
        self.SLIDER_X_PLUS      = Rect(873,861,25,31)
        self.SLIDER_Y_MINUS     = Rect(415,931,21,30)
        self.SLIDER_Y_PLUS      = Rect(872,932,27,29)
        self.NEXT_BUTTON_COORDS = Rect(800,975,100,80)
        self.BIG_RED_BUTTON     = Rect(917,863,95,91)
        # END CONSTANTS

        # MORE CONSTANTS
        self.YELLOW = (250,   167,   74)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)

    @property
    def is_player_1(self):
        # note it returns the opposite as each player uses the other players allocation board to play with
        return not self._allocation.is_player_1()

    @property
    def shot_taken(self):
        return self._shot_taken

    @property
    def swap_player(self):
        return self._swap_player

    @swap_player.setter
    def swap_player(self, value):
        self._swap_player = value

    def reset_shot_taken(self):
        self._shot_taken = False

    def take_turn(self, pos, event):
            
        #self._allocation.show_allocation(self._screen)
        player1_name = self._dal.get_logged_user_player_1().username;
        player2_name = self._dal.get_logged_user_player_2().username;
        self._facade.DrawStringArchivoNarrow(self._screen,player1_name, 26, 240,self.WHITE, False, 44 )
        self._facade.DrawStringArchivoNarrow(self._screen,player2_name, 1100, 240,self.GREEN, False, 44 )

        if self.shot_taken == False:
            self._player_input(pos, event)
        else:
            self._next_player_process(pos, event)

        self._board.draw(self._allocation)

    def _next_player_process(self, pos, event):

        player1_name = self._dal.get_logged_user_player_1().username;
        player2_name = self._dal.get_logged_user_player_2().username;
        player1_msg = "The next player is {}. Click to contine.".format(player1_name)
        player2_msg = "The next player is {}. Click to contine.".format(player2_name)


        if not self._allocation.is_player_1() == True:
            self._facade.DrawStringArchivoNarrow(self._screen,player2_msg, 400, 980,self.YELLOW, False )
        else:
            self._facade.DrawStringArchivoNarrow(self._screen,player1_msg, 400, 980,self.YELLOW, False )

        self._board.draw_next_button()   

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._next_button_coords.collidepoint(pos) == True:
                self._swap_player = True
                self._next_player = False

    def _player_input(self,pos, event):
        
        # if we have let go of the mouse button i.e. MOUSE BUTTON is TRUE 
        # and we are over the SLIDER MINUS BUTTON for the X Slider
        # then set the classes _ready flag to True
        # this is to stop the repetition of mouse clicks between 
        # mouse down and mouse up

        if event.type == pygame.MOUSEBUTTONUP:
            if self.SLIDER_X_MINUS.collidepoint(pos) == True:
                self._ready = True
        
        # see above comment for explanation
        if event.type == pygame.MOUSEBUTTONUP:
            if self.SLIDER_X_PLUS.collidepoint(pos) == True:
                self._ready = True
        
        # see above comment for explanation
        if event.type == pygame.MOUSEBUTTONUP:
            if self.SLIDER_Y_MINUS.collidepoint(pos) == True:
                self._ready = True
        
        # see above comment for explanation
        if event.type == pygame.MOUSEBUTTONUP:
            if self.SLIDER_Y_PLUS.collidepoint(pos) == True:
                self._ready = True

        # When the mouse button is pressed on slider control
        # and we are ready to process the message
        # the increment or decrement the variable that keeps track of
        # where we are on the slider

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.SLIDER_X_MINUS.collidepoint(pos) == True:
                if self._ready == True:
                    self._control_x_col = self._control_x_col - 1
                    self._ready = False
                    if self._control_x_col < 0:     # stop us from going off the end of the slider
                        self._control_x_col = 0

        # see above comment for explanation
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.SLIDER_X_PLUS.collidepoint(pos) == True:
                if self._ready == True:
                    self._control_x_col = self._control_x_col + 1
                    self._ready = False
                    if self._control_x_col >= self._board_width:       # stop us from going off the end of the slider
                        self._control_x_col = self._board_width       

        # see above comment for explanation
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.SLIDER_Y_MINUS.collidepoint(pos) == True:
                if self._ready == True:
                    self._control_y_row = self._control_y_row - 1
                    self._ready = False
                    if self._control_y_row < 0:
                        self._control_y_row = 0

        # see above comment for explanation
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.SLIDER_Y_PLUS.collidepoint(pos) == True:
                if self._ready == True:
                    self._control_y_row = self._control_y_row + 1
                    self._ready = False
                    if self._control_y_row >= self._board_height:
                        self._control_y_row = self._board_height     
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.BIG_RED_BUTTON.collidepoint(pos) == True:
                if self._ready == True:
                   self.Fire()
        
        #####################################################
        # These are drawing the yellow squares on the sliders                
        x = 460 + (self._control_x_col * 30 )

        pygame.draw.line(self._screen, self.YELLOW, (x, 860), (x,880), 15)

        x = 460 + (self._control_y_row * 35 )
        pygame.draw.line(self._screen, self.YELLOW, (x, 933), (x,953), 15)

        ## draw the select item on screen
        
        self._display_x, self._display_y = self._board.array_coords_to_user_coords( self._control_x_col , self._control_y_row )
        self._facade.DrawStringArchivoNarrow(self._screen,str(self._display_x), 301, 896,self.WHITE, False )
        self._facade.DrawStringArchivoNarrow(self._screen,str(self._display_y), 301, 973,self.WHITE, False )
    
    def Fire(self):
        self._next_player = True
        self._shot_taken = True

        s = self._allocation.get_square_value( self._control_y_row, self._control_x_col )
      
        if s == "B":
            self._allocation.set_square_value_kill(self._control_y_row, self._control_x_col)
            self._allocation.battleship_hit()
        elif s == "C":
            self._allocation.set_square_value_kill(self._control_y_row, self._control_x_col )
            self._allocation.carrier_hit()
        elif s == "S":
            self._allocation.set_square_value_kill( self._control_y_row, self._control_x_col )
            self._allocation.submarine_hit()
        elif s == "R":
            self._allocation.set_square_value_kill( self._control_y_row, self._control_x_col )
            self._allocation.cruiser_hit()
        elif s == "D":
            self._allocation.set_square_value_kill( self._control_y_row, self._control_x_col )
            self._allocation.destroyer_hit()
        elif s == "K":
            self._allocation.set_square_value_kill(self._control_y_row, self._control_x_col )
            
        else:
            self._allocation.set_square_value_miss(self._control_y_row, self._control_x_col)
