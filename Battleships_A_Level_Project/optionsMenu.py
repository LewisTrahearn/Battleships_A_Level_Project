import pygame
from pygame.locals import *
import facade_layer as Facade
import login as LoginScreen
from enum import Enum
import GameBoard as GameScreen
import Register as RegisterScreen
import ShipsLog as ShipsLogScreen

from navigate import Navigate

class Button(Enum):
    """
    A list of valid enumeration types to be used across
    all classes for navigation between screens.

    """

    SIMULATION = 1
    OPPONENT = 2
    PROFILE = 3
    SHIPS_LOG = 4
    HELP = 5
    QUIT = 6
    CONTINUE = 7



class optionsMenu(object):
    """description of class"""

    def __init__(self):
        """ default constructor """
        self._PLAYER2 = 2
        self._login_color = 255, 0, 0
        self._facade = Facade.facade_layer()
        self._btn_simulation_off = self._facade.loadImage("simulation_button_off.png")
        self._btn_simulation_on = self._facade.loadImage("simulation_button_on.png")
        self._btn_simulation_pos = Rect(26, 140, 322, 72)

        self._btn_opponent_off = self._facade.loadImage("opponent_button_off.png")
        self._btn_opponent_on = self._facade.loadImage("opponent_button_on.png")
        self._btn_opponent_pos = Rect(26, 240, 322, 72)

        self._btn_profile_off = self._facade.loadImage("profile_button_off.png")
        self._btn_profile_on = self._facade.loadImage("profile_button_on.png")
        self._btn_profile_pos = Rect(26, 340, 322, 72)

        self._btn_ships_log_off = self._facade.loadImage("ships_log_button_off.png")
        self._btn_ships_log_on = self._facade.loadImage("ships_log_button_on.png")
        self._btn_ships_log_pos = Rect(26, 440, 322, 72)

        self._btn_help_off = self._facade.loadImage("help_button_off.png")
        self._btn_help_on = self._facade.loadImage("help_button_on.png")
        self._btn_help_pos = Rect(26, 540, 540, 72)

        self._btn_quit_off = self._facade.loadImage("quit_button_off.png")
        self._btn_quit_on = self._facade.loadImage("quit_button_on.png")
        self._btn_quit_pos = Rect(26, 915, 322, 72)

        self._instruction_box_simulation = self._facade.loadImage("instructions_box_simulation.png")
        self._instruction_box_ships_log = self._facade.loadImage("instructions_box_ships_log.png")
        self._instruction_box_opponent = self._facade.loadImage("instructions_box_opponent.png")
        self._instruction_box_profile = self._facade.loadImage("instructions_box_profile.png")
        self._play_button = self._facade.loadImage("play_button.png")
        self._login_button = self._facade.loadImage("login_button.png")
        self._edit_button = self._facade.loadImage("edit_button.png")


        self._play_button_pos = Rect(950,875,198,63)
        self._login_button_pos = Rect(436,875,198,63)
        self._instruction_box_pos = Rect(436,32,804,422)
        self._edit_button_pos = Rect(436,875,198,63)

        self._current_button = Button.SIMULATION
        self._current_selected = Button.SIMULATION
        self._screen_size = Rect(0, 0, 1280, 1024,)

    def process(self, pos, event, screen, dal):
     # this is the login button for player 2. This allows the second player to login only when the gamemode is against an opponent
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._current_selected == Button.OPPONENT:
                if self._login_button_pos.collidepoint(pos) == True:    
                    #This is used to login player 2
                    login = LoginScreen.Login(0, 0, 1280, 1024, dal, 2)
                    retval = login.display()
                    screen1, background1, clock1 = self._facade.initialise_screen("battleships", "battleship_Options_leftbar.png", self._screen_size)
                    self.draw(screen, Button.OPPONENT, Button.OPPONENT,dal)
                    if retval == Navigate.SPLASHSCREEN:
                        return retval
                      

        # this calls the game board for the opponent when the play button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._current_selected == Button.OPPONENT:
                if self._play_button_pos.collidepoint(pos) == True:
                    game = GameScreen.GameBoard(0,0,1280,1024,dal)
                    retval = game.display() 
                    screen1, background1, clock1 = self._facade.initialise_screen("battleships", "battleship_Options_leftbar.png", self._screen_size)
                    self.draw(screen, Button.OPPONENT, Button.OPPONENT,dal)
                    if retval == Navigate.SPLASHSCREEN:
                        return retval



        # this calls the game board for the simulation when the play button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._current_selected == Button.SIMULATION:
                if self._play_button_pos.collidepoint(pos) == True:
                    #here we need to auto login CPU as player 2
                    dal.is_user_valid("CPU", "CPU",self._PLAYER2)
                    game = GameScreen.GameBoard(0,0,1280,1024,dal)
                    retval = game.display() 
                    screen1, background1, clock1 = self._facade.initialise_screen("battleships", "battleship_Options_leftbar.png", self._screen_size)
                    self.draw(screen, Button.SIMULATION, Button.SIMULATION,dal)
                    if retval == Navigate.SPLASHSCREEN:
                        return retval


        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._current_selected == Button.PROFILE:
                if self._edit_button_pos.collidepoint(pos) == True:
                    register = RegisterScreen.Register(0, 0, 1280, 1024, dal, True)
                    retval = register.display() 
                    screen1, background1, clock1 = self._facade.initialise_screen("battleships", "battleship_Options_leftbar.png", self._screen_size)
                    self.draw(screen, Button.PROFILE, Button.PROFILE, dal)
                    if retval == Navigate.SPLASHSCREEN:
                        return retval
                    
        # this calls the game board for the simulation when the play button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._current_selected == Button.SHIPS_LOG:
                if self._play_button_pos.collidepoint(pos) == True:
                    #here we need to auto login CPU as player 2
                    ships_log = ShipsLogScreen.ShipsLog(0,0,1280,1024,dal)
                    retval = ships_log.display()

                    screen1, background1, clock1 = self._facade.initialise_screen("battleships", "battleship_Options_leftbar.png", self._screen_size)
                    self.draw(screen, Button.SIMULATION, Button.SIMULATION,dal)
                    if retval == Navigate.SPLASHSCREEN:
                        return retval

                            
     # this tells the players who is against who only displayed for the opponent and also if another player is logged in.
        if self._current_selected == Button.OPPONENT:
            if dal.is_player_two_logged_in() == True:
                message = "Player {} v Player {}".format(dal.get_logged_user_player_1().username, dal.get_logged_user_player_2().username)
                self._facade.DrawStringArchivoNarrow(screen, message, 436, 700, self._login_color, False, 60)
     # displays player 1 vs CPU and will only display for the simulation section
        if self._current_selected == Button.SIMULATION:
                message = "Player {} v Computer".format(dal.get_logged_user_player_1().username)
                self._facade.DrawStringArchivoNarrow(screen, message, 436, 700, self._login_color, False, 60)
     
     # while the mouse is moving this decides if the mouse hovered on a button and if it did it tells it to highlight it.
        if event.type == pygame.MOUSEMOTION:
            if self._btn_simulation_pos.collidepoint(pos) == True:
               self._current_button = Button.SIMULATION
            
            if self._btn_opponent_pos.collidepoint(pos) == True:
               self._current_button = Button.OPPONENT

            if self._btn_ships_log_pos.collidepoint(pos) == True:
               self._current_button = Button.SHIPS_LOG

            if self._btn_profile_pos.collidepoint(pos) == True:
               self._current_button = Button.PROFILE

            if self._btn_help_pos.collidepoint(pos) == True:
               self._current_button = Button.HELP

            if self._btn_quit_pos.collidepoint(pos) == True:
               self._current_button = Button.QUIT

     # this is for when a person clicks a button this keeps track of the currnetly selected button 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._btn_simulation_pos.collidepoint(pos) == True:
               self._current_selected = Button.SIMULATION
            
            if self._btn_opponent_pos.collidepoint(pos) == True:
               self._current_selected = Button.OPPONENT

            if self._btn_ships_log_pos.collidepoint(pos) == True:
               self._current_selected = Button.SHIPS_LOG

            if self._btn_profile_pos.collidepoint(pos) == True:
               self._current_selected = Button.PROFILE

            if self._btn_help_pos.collidepoint(pos) == True:
               self._current_selected = Button.HELP

            if self._btn_quit_pos.collidepoint(pos) == True:
               self._current_selected = Button.QUIT

            if self._current_selected == Button.QUIT:
                return Button.QUIT
      #draws the buttons according to the current state
        self.draw(screen,self._current_button, self._current_selected, dal)

        return Button.CONTINUE
    
    def draw(self, screen, button_on, instructions, dal):
        
        """ public method to draw the menu to the screen """
        if button_on == Button.SIMULATION:
            screen.blit(self._btn_simulation_on, self._btn_simulation_pos)
        else:
            screen.blit(self._btn_simulation_off, self._btn_simulation_pos)

        if instructions == Button.SIMULATION:
             screen.blit(self._instruction_box_simulation, self._instruction_box_pos)
             screen.blit(self._play_button, self._play_button_pos)

        if instructions == Button.OPPONENT:
             screen.blit(self._instruction_box_opponent, self._instruction_box_pos)
             if dal.is_player_two_logged_in() == True:
                screen.blit(self._play_button, self._play_button_pos)
             screen.blit(self._login_button, self._login_button_pos)

        if instructions == Button.SHIPS_LOG:
             screen.blit(self._instruction_box_ships_log, self._instruction_box_pos)
             screen.blit(self._play_button, self._play_button_pos)

        if instructions == Button.PROFILE:
             screen.blit(self._instruction_box_profile, self._instruction_box_pos)
             screen.blit(self._edit_button, self._edit_button_pos)


       
        if button_on == Button.OPPONENT:
            screen.blit(self._btn_opponent_on, self._btn_opponent_pos)
        else:
            screen.blit(self._btn_opponent_off, self._btn_opponent_pos)
       
        if button_on == Button.PROFILE:
            screen.blit(self._btn_profile_on, self._btn_profile_pos)
        else:
            screen.blit(self._btn_profile_off, self._btn_profile_pos)

        if button_on == Button.SHIPS_LOG:
            screen.blit(self._btn_ships_log_on, self._btn_ships_log_pos)
        else:
            screen.blit(self._btn_ships_log_off, self._btn_ships_log_pos)

        if button_on == Button.HELP:
            screen.blit(self._btn_help_on, self._btn_help_pos)
        else:
            screen.blit(self._btn_help_off, self._btn_help_pos)

        if button_on == Button.QUIT:
            screen.blit(self._btn_quit_on, self._btn_quit_pos)
        else:
            screen.blit(self._btn_quit_off, self._btn_quit_pos)





