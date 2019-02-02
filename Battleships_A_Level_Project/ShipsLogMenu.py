import pygame
from pygame.locals import *
import facade_layer as Facade
import login as LoginScreen
from enum import Enum
import GameBoard as GameScreen
import Register as RegisterScreen
import ShipsLog as ShipsLogScreen

from navigate import Navigate

class MenuOptionButton(Enum):
    """
    A list of valid enumeration types to be used across
    all classes for navigation between screens.

    """

    YOUR_PROFILE = 1
    LEAST_HITS = 2
    LEAST_TIME = 3
    MOST_WINS = 4
    EXIT = 5


class ShipsLogMenu(object):
    """description of class"""

    def __init__(self, screen, dal):
        """ default constructor """

        self._screen = screen
        self._dal = dal
        self._facade = Facade.facade_layer()

        #### PROFILE BUTTON STATES
        self._btn_profile_mouseover = self._facade.loadImage("your_profile_white_mouseover.png")
        self._btn_profile_normal = self._facade.loadImage("your_profile_white_normal.png")
        self._btn_profile_selected = self._facade.loadImage("Your Profile_mousedown.png")

        #### LEAST HITS BUTTON STATES
        self._btn_least_hits_mouseover = self._facade.loadImage("least_hits_mouseover.png")
        self._btn_least_hits_normal = self._facade.loadImage("least_hits_normal.png")
        self._btn_least_hits_selected = self._facade.loadImage("least_hits_mousedown.png")

        #### LEAST TIME BUTTON STATES
        self._btn_least_time_mouseover = self._facade.loadImage("least time_mouseover.png")
        self._btn_least_time_normal = self._facade.loadImage("least time_normal.png")
        self._btn_least_time_selected = self._facade.loadImage("least time_mousedown.png")

        #### MOST WINS BUTTON STATES
        self._btn_most_wins_mouseover = self._facade.loadImage("most wins_mouseover.png")
        self._btn_most_wins_normal = self._facade.loadImage("most wins_normal.png")
        self._btn_most_wins_selected = self._facade.loadImage("most wins_mousedown.png")

        #### EXIT BUTTON STATES
        self._btn_exit_mouseover = self._facade.loadImage("exit_mouseover.png")
        self._btn_exit_normal = self._facade.loadImage("exit_normal.png")
        self._btn_exit_selected = self._facade.loadImage("exit_mousedown.png")

        self._your_profile = Rect(0,198,322,124)
        self._least_hits = Rect(0,344,322,124)
        self._least_time = Rect(0,480,322,124)
        self._most_wins = Rect(0,618,322,124)
        self._exit = Rect(0,738,322,124)

        self._current_button = MenuOptionButton.LEAST_TIME
        self._current_selected = MenuOptionButton.YOUR_PROFILE

    def process(self, pos, event):

  # while the mouse is moving this decides if the mouse hovered on a button and if it did it tells it to highlight it.
        if event.type == pygame.MOUSEMOTION:
            if self._your_profile.collidepoint(pos) == True:
               self._current_button = MenuOptionButton.YOUR_PROFILE
    
            if self._least_hits.collidepoint(pos) == True:
               self._current_button = MenuOptionButton.LEAST_HITS

            if self._least_time.collidepoint(pos) == True:
               self._current_button = MenuOptionButton.LEAST_TIME

            if self._most_wins.collidepoint(pos) == True:
               self._current_button = MenuOptionButton.MOST_WINS

            if self._exit.collidepoint(pos) == True:
               self._current_button = MenuOptionButton.EXIT



     # this is for when a person clicks a button this keeps track of the currnetly selected button 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._your_profile.collidepoint(pos) == True:
               self._current_selected = MenuOptionButton.YOUR_PROFILE
    
            if self._least_hits.collidepoint(pos) == True:
               self._current_selected = MenuOptionButton.LEAST_HITS

            if self._least_time.collidepoint(pos) == True:
               self._current_selected = MenuOptionButton.LEAST_TIME

            if self._most_wins.collidepoint(pos) == True:
               self._current_selected = MenuOptionButton.MOST_WINS

            if self._exit.collidepoint(pos) == True:
               self._current_selected = MenuOptionButton.EXIT


            #draws the buttons according to the current state
        self._draw_mouse_over()
        self._draw_selected()

    def _draw_mouse_over(self):
        
        if self._current_button == MenuOptionButton.YOUR_PROFILE:
            self._screen.blit(self._btn_profile_mouseover, self._your_profile)

        if self._current_button == MenuOptionButton.LEAST_HITS:
            self._screen.blit(self._btn_least_hits_mouseover, self._least_hits)

        if self._current_button == MenuOptionButton.LEAST_TIME:
            self._screen.blit(self._btn_least_time_mouseover, self._least_time)

        if self._current_button == MenuOptionButton.MOST_WINS:
            self._screen.blit(self._btn_most_wins_mouseover, self._most_wins)

        if self._current_button == MenuOptionButton.EXIT:
            self._screen.blit(self._btn_exit_mouseover, self._exit)


    def _draw_selected(self):

        if self._current_selected == MenuOptionButton.YOUR_PROFILE:
            self._screen.blit(self._btn_profile_selected, self._your_profile)

        if self._current_selected == MenuOptionButton.LEAST_HITS:
            self._screen.blit(self._btn_least_hits_selected, self._least_hits)

        if self._current_selected == MenuOptionButton.LEAST_TIME:
            self._screen.blit(self._btn_least_time_selected, self._least_time)

        if self._current_selected == MenuOptionButton.MOST_WINS:
            self._screen.blit(self._btn_most_wins_selected, self._most_wins)

        if self._current_selected == MenuOptionButton.EXIT:
            self._screen.blit(self._btn_exit_selected, self._exit)