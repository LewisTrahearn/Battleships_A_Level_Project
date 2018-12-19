"""
Module Name:
    MenuPointer.py

Functions/Methods:
        __init__(self) Constructor - pass in screen size
        process - public method that decides how and where the pointer will be shown based upon the external mouse coords passed in
        _clear_colors - private helper method to reset/clear all colors to black
        _move_to_login - private method to move the pointer to login position
        _move_to_register - private method to move the pointer to _move_to_register position
        _move_to_quit -  private method to move the pointer to _move_to_register position
        draw - public method to draw the menu to the screen

Class:
    MenuPointer - move and draw menu for splashscreen

Imports:
    pygame - python gaming library
    os - operating system functions, in our case allows access to directory paths.

Purpose:
    Control the Menu Pointer on the splashscreen (a ship image), to move
    according to the mouse over of certain areas.
    
Author:
    Lewis Trahearn

"""

import os 
import pygame
from pygame.locals import *


import facade_layer as Facade
from navigate import Navigate

class MenuPointer():
    """
    description:
        Control the Menu Pointer on the splashscreen (a ship image), to move
        according to the mouse over of certain areas.
    
    attributes:
        _login_link         private variable that defines a screen area that is deemed to be selected.
        _register_link      private variable that defines a screen area that is deemed to be selected.
        _quit_link          private variable that defines a screen area that is deemed to be selected.
        _login_color        private variable that defines the menu color 
        _register_color     private variable that defines the menu color
        _quit_color         private variable that defines the menu color
        _x                  private variable that defines x position for the pointer
        _y                  private variable that defines y position for the pointer
        _selected_option    private variable that defines currently selected option
        _file               private variable that defines the menu pointer file name
        _main_dir           private variable that defines the folder where the pointer image resides
        _image              private variable that is used to hold the loaded image
        _rect               private variable that is used to hold the loaded image dimensions
        _width              private variable that is used to hold the loaded image width
        _height             private variable that is used to hold the loaded image height

    methods:
        __init__(self) Constructor
        process - public method that decides how and where the pointer will be shown based upon the external mouse coords passed in
        _clear_colors - private helper method to reset/clear all colors to black
        _move_to_login - private method to move the pointer to login position
        _move_to_register - private method to move the pointer to register position
        _move_to_quit -  private method to move the pointer to quit position
        draw - public method to draw the menu to the screen
    """   

    def __init__(self):
        """ default constructor """
        self._login_color = 0, 0, 0
        self._register_color = 0, 0, 0
        self._quit_color = 0, 0, 0
        self._x = 0
        self._y = 0
        self._selected_option = ""
        
        self._file = "MenuPointer.png"
        self._main_dir = os.path.split(os.path.abspath(__file__))[0]
        self._file = os.path.join(self._main_dir, 'images', self._file)

        self._login_link = Rect(78, 366, 243, 134)
        self._register_link = Rect(62, 554, 451, 109)
        self._quit_link = Rect(80, 724, 205, 147)


        self._image = pygame.image.load(self._file).convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self._rect = self._image.get_rect()
        self._width = self._rect.width
        self._height = self._rect.height
        self._move_to_login()

        self._facade = Facade.facade_layer()

    def selected(self, pos):
        
        returnVal = None

        if self._register_link.collidepoint(pos) == True:
            returnVal = Navigate.REGISTER

        if self._login_link.collidepoint(pos) == True:
            returnVal = Navigate.LOGIN

        if self._quit_link.collidepoint(pos) == True:
            returnVal = Navigate.QUIT_SPLASHSCREEN

        return returnVal

    def process(self, pos):
        """ public method that decides how and where the pointer will be shown based upon the external mouse coords passed in """        
        if self._register_link.collidepoint(pos) == True:
            self._move_to_register()
            self._facade.playRolloverSound("register")


        if self._login_link.collidepoint(pos) == True:
            self._move_to_login()
            self._facade.playRolloverSound("login")


        if self._quit_link.collidepoint(pos) == True:
            self._move_to_quit()
            self._facade.playRolloverSound("quit")        


    def _clear_colors(self):
        """ private helper method to reset/clear all colors to black """
        self._login_color = 0, 0, 0
        self._register_color = 0, 0, 0
        self._quit_color = 0, 0, 0

    def _move_to_login(self):
        """ private method to move the pointer to login position """
        self._x = 600
        self._y = 350
        self._selected_option = "login"
        self._clear_colors()
        self._login_color = 255, 255, 255

    def _move_to_register(self):
        """ private method to move the pointer to register position """
        self._x = 600
        self._y = 550
        self._selected_option = "register"
        self._clear_colors()
        self._register_color = 255, 255, 255

    def _move_to_quit(self):
        """ private method to move the pointer to quit position """
        self._x = 600
        self._y = 750
        self._selected_option = "quit"
        self._clear_colors()
        self._quit_color = 255, 255, 255

    def draw(self, screen):
        """ public method to draw the menu to the screen """

        self._facade.DrawStringPirateFont(screen, "Login", 85, 320, self._login_color, False)
        self._facade.DrawStringPirateFont(screen, "Register", 85, 500, self._register_color, False)
        self._facade.DrawStringPirateFont(screen, "Quit", 85, 690, self._quit_color, False)


        self._rect.x = self._x
        self._rect.y = self._y
        screen.blit(self._image, self._rect)

       
        



