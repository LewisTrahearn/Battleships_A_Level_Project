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

"""
import pygame
from pygame.locals import *
from navigate import Navigate
import facade_layer as Facade
import pygame_textinput 

class Field():
    """
    This is a container class for each field within the system
    """

    def __init__(self, fieldname, textinput, x1, y1):
        """This is the constructor for the class:
            - parameters 
                :param fieldname:    - name you wish to call the field
                :param textinput:    - field object
                :param x:            - the x coordinate of the field
                :param y:            - the y coordinate of the field
            - type of parameters
                :type fieldname: string literal
                :type textinput: object pygame_textinput 
                :type x: int 
                :type y: int 
            - return
                :return: none since its a constructor
            - return type
                :rtype: not applicable

        """
        self.fieldname = fieldname
        self.textinput = textinput
        self.x1 = x1
        self.y1 = y1


class Login():
    """
    description:
        This class represents the splashscreen that will introduce the user to the game
        and give them the options of either logging in, registering themselves in the game 
        or quitting.
    
    attributes:
        _screen_size    private variable, defines screen size as passed in to the constructor of the class\n
        _login_link     private variable that defines a screen area that is deemed to be selected.\n
        _register_link  private variable that defines a screen area that is deemed to be selected.
        _quit_link      private variable that defines a screen area that is deemed to be selected.
 
        _enum_navigate  private object that defines enumeration types for navigation
        _facade         private object that defines the facade layer between pygame and our class
        _background     private object from pygame that represents the background

    methods:
        __init__(self, x1, y1, w, h) Constructor - pass in screen size



    """
    def __init__(self, x1, y1, w, h, dal, player = 1):
        """ 
        Constructor - passes dimension of screen size.

        Parameters:
        x1 - x - coord
        y1 - y - coord
        w - width
        h - height
        """
        self._dal = dal
        self._form = []
        self._form_index = 0
        self._text_color = (22, 22, 54)
        self._username = None
        self._password = None
        self._screen_size = Rect(x1, y1, w, h)
        self._player = player

        self._facade = Facade.facade_layer()
        self._submit_button = Rect(426,656,207,58)
        self._cancel_button = Rect(686,662,207,58)


    def display(self):
        """ """
        screen, background, clock = self._facade.initialise_screen("battleships", "loginScreen.png", self._screen_size)

        self._build_form()

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self._submit_button.collidepoint(pos) == True:
                        if self._is_login_valid() == True:
                            return Navigate.OPTIONS

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self._cancel_button.collidepoint(pos) == True:
                        return Navigate.SPLASHSCREEN
            

            screen.blit(background, (0, 0))

            
            self._process_form(screen, events)

            pygame.display.update()

            pygame.display.flip()

    def _is_login_valid(self):
        return_value = False

        self._username = self._form[0].textinput.get_text()
        self._password = self._form[1].textinput.get_text()
        if self._dal.is_user_valid(self._username, self._password,self._player):
            return_value = True

        return return_value


    def _build_form(self):
        """ """
        self._username = pygame_textinput.TextInput('tahoma', 30, True, self._text_color, self._text_color, 400, 35)
        self._password = pygame_textinput.TextInput('tahoma', 30, True, self._text_color, self._text_color, 400, 35)
        # now create a field object for each one and add it to the forms array
        
        self._form.append(Field("username", self._username, 444, 345))
        self._form.append(Field("password", self._password, 444, 474))

        # now set the index of the form that should be input first
        self._form_index = 0


    def _process_form(self, screen, events):
        """ """
        idx = self._form_index
        currentField = self._form[idx]
        currentInput = currentField.textinput

        retVal = currentInput.update(events)

        if retVal == True:
            self._form_index += 1
            if self._form_index >= len(self._form):
                self._form_index = 0
            # Blit its surface onto the screen
        for fld in self._form:
            screen.blit(fld.textinput.get_surface(), (fld.x1, fld.y1))
