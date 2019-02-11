r"""Module Name:

    login.py

Public Functions/Methods:

    display

Class:
    Field - This is a container class used to hold each form control
    Login - This is the main login class used to load the screen and handle the login process

Imports:

    **import pygame**   - pygame library.

    **pygame.locals**   - this is needed for the Rect definition.

    **enum_navigate**   - common enumeration values shared across all classes.

    **facade_layer**    - an abstraction from the pygame module, for certain common functions.

    **Navigate**        - This class is an enumeration class that holds all the options required to move around the system.
    
    **pygame_textinput** - a 3rd party text input class that allows text input

Purpose:
    This module contains two classes the Field class and the Login class.
    The login class is used to load the screen, build a form, get the
    user input and then call the data access layer in order to determine
    if its correct or not.

    The Field class a a simple container class that allows me to collect the information
    for each input field, such as the x,y coords and instance of the pygame_textinput
    and the name of the field and then put these into an array to allow me to cycle around
    the form.
    
Author:
    Lewis Trahearn
______________________________________________________________________________________________________________________



"""



import pygame
from pygame.locals import *


from navigate import Navigate

import facade_layer as Facade
import optionsMenu as Menu
import Board as Board
import Allocation as Allocation
import player as Player
import ComputerPlayer as CPU
import TrackTime as StopWatch








class GameBoard(object):
    """
    description:
        This class represents the splashscreen that will introduce the user to the game
        and give them the options of either logging in, registering themselves in the game 
        or quitting.
    
    attributes:
        _screen_size    private variable, defines screen size as passed in to the constructor of the class
        _login_link     private variable that defines a screen area that is deemed to be selected.
        _register_link  private variable that defines a screen area that is deemed to be selected.
        _quit_link      private variable that defines a screen area that is deemed to be selected.
 
        _enum_navigate  private object that defines enumeration types for navigation
        _facade         private object that defines the facade layer between pygame and our class
        _background     private object from pygame that represents the background

    methods:
        __init__(self, x1, y1, w, h) Constructor - pass in screen size
        changed


    """
    def __init__(self, x1, y1, w, h, dal):
        """ 
        Constructor - passes dimension of screen size.

        Parameters:
        x1 - x - coord
        y1 - y - coord
        w - width
        h - height
        """
        self._dal = dal
        self._screen_size = Rect(x1, y1, w, h)

        self._facade = Facade.facade_layer()
        self.checked_out = False

        # RGB Colors for the colours we are using
        self.BLACK = (  0,   0,   0)
        self.WHITE = (255, 255, 255)
        self.BLUE =  (  0,   0, 255)
        self.GREEN = (  0, 255,   0)
        self.RED =   (255,   0,   0)
        self.YELLOW = (250,   167,   74)
        self.PURPLE = (242,   102,   230)
        self.OTHER = (240,204,7)


    def display(self):
        """ """
        screen, background, clock = self._facade.initialise_screen("battleships", "BATTLESHIPS.png", self._screen_size)

        board = Board.Board(screen, self._dal)

        p1_allocation = Allocation.Allocation(1)
        p2_allocation = Allocation.Allocation(2)

        Tracker = StopWatch.TrackTime()
        

        player1 = Player.Player(board, p2_allocation, self._dal, screen)
        if self._dal.is_player2_cpu() == False:
            player2 = Player.Player(board, p1_allocation, self._dal, screen)
        else: 
            player2 = CPU.ComputerPlayer(board, p1_allocation, self._dal, screen)


        current_player = player1

        Tracker.start_timer_1()   ## Start tracking the time taken by player 

        ################################################
        # This is the main gaming loop for this screen
        ################################################
        while True:

            #cap the framerate to 30 frames per second
            clock.tick(30)

            # this loop will walk through a list of captured events
            # and react according to the specific ones we are interested in.
            events = pygame.event.get()

            for event in events:
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return Navigate.SPLASHSCREEN
                
                ## Get the current mouse positional information
                pos = pygame.mouse.get_pos()
            
            screen.blit(background, (0, 0))


            if p1_allocation.are_all_ships_destroyed() == False and p2_allocation.are_all_ships_destroyed() == False and self.checked_out == False:
                current_player.take_turn(pos, event)
                if current_player.swap_player == True:
                    current_player.swap_player = False
                    current_player.reset_shot_taken()
                    if current_player.is_player_1 == True:
                        Tracker.stop_timer_1()
                        Tracker.start_timer_2()
                        current_player = player2
                    else:
                        Tracker.stop_timer_2()
                        Tracker.start_timer_1()
                        current_player = player1
            else:
                self.checked_out == True
                t1 = Tracker.get_overall_time_for_timer_1()
                t2 = Tracker.get_overall_time_for_timer_2()
                shots1 = p1_allocation.get_number_of_shots_taken
                shots2 = p2_allocation.get_number_of_shots_taken

                if p1_allocation.are_all_ships_destroyed() == True:  ### then player 2 won
                    self._facade.DrawStringArchivoNarrow(screen,"GAME OVER PLAYER 2 WINS", 400, 438,self.GREEN, False, 77 )
                    self._dal.add_stat_to_player(2,t2, str(shots2), "true")
                    self._dal.add_stat_to_player(1,t1, str(shots1), "false")
                else: ## player 1 won
                    self._facade.DrawStringArchivoNarrow(screen,"GAME OVER PLAYER 1 WINS", 400, 438,self.GREEN, False, 77 )
                    self._dal.add_stat_to_player(1,t1, str(shots1), "true")
                    self._dal.add_stat_to_player(2,t2, str(shots2), "false")

         

            
            # the next statement is important otherwise carriage returns will remain and continue to be processed in the processForm           

            pygame.display.update()
         
            
            pygame.display.flip()



