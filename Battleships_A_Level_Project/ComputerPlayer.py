import pygame
from player import Player
from pygame.locals import *
from navigate import Navigate
import DataAcessLayer as DataAccessLayer
import Board as Board
import Allocation as Allocation
import facade_layer as Facade

from player import Player


class ComputerPlayer(Player):
    """description of class"""
    def __init__(self, board, allocation, dal, screen):
        super(ComputerPlayer, self).__init__( board, allocation, dal, screen)



    def _player_input(self,pos, event):
        

        # When the mouse button is pressed on slider control
        # and we are ready to process the message
        # the increment or decrement the variable that keeps track of
        # where we are on the slider


        #for the computer we need to do the following:
        #for level 1 we need to randomly select the _control_x_col and _control_y_row
        #in the range and then call the fire 
        self._control_x_col,self._control_y_row = self._allocation.get_random_position()
        self.Fire()
         
        
        


    def take_turn(self, pos, event):
            
        #self._allocation.show_allocation(self._screen)
        player1_name = self._dal.get_logged_user_player_1().username;
        player2_name = self._dal.get_logged_user_player_2().username;
        self._facade.DrawStringArchivoNarrow(self._screen,player1_name, 26, 240,self.WHITE, False, 44 )
        self._facade.DrawStringArchivoNarrow(self._screen,player2_name, 1100, 240,self.GREEN, False, 44 )


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

        if self.shot_taken == False:
            self._player_input(pos, event)
        else:
            self._next_player_process(pos, event)

        self._board.draw(self._allocation)


