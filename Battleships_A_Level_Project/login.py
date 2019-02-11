r"""**Module Name:**
    *login.py*

**Public Functions/Methods:**
    *display* - This loads and processes the entire screen

**Class:**
    Login - This is the main login class used to load the screen and handle the login process

**Imports:**

    *import pygame*   - pygame library.

    *pygame.locals*   - this is needed for the Rect definition.

    *enum_navigate*   - common enumeration values shared across all classes.

    *facade_layer*    - an abstraction from the pygame module, for certain common functions.

    *Navigate*        - This class is an enumeration class that holds all the options required to move around the system.
    
    *pygame_textinput* - a 3rd party text input class that allows text input

    *Field*            - a simple container class to hold form information

**Purpose:**
    This module containsthe Login class. The login class is used to load 
    the screen, build a form, get the user input and then call the data access layer 
    in order to determine if the user is valid.

**Author:**
    *Lewis Trahearn*

"""


import pygame
from pygame.locals import *
from navigate import Navigate
import facade_layer as Facade
import pygame_textinput 
from Field import *

class Login():
    """
    **description:**
        This class deals totally with the login functionality and has one public entry point
        which is the display method. This class is used to login the initial player and later on 
        to login the second player in the two player mode.
        
        This then handles the following functionality:
            #. loads the screen
            #. gets the users username and login details
            #. calls into the data access layer in order to verify the details.
    
    **attributes:**
        
        **private instance variables/attributes**

        *self._dal* - data access object that is passed in

        *self._form* - this is a form array, which is used to hold the two fields

        *self._form_index* - this keeps track of where we are in the form and what the current field is.

        *self._text_color* - colo of the text used while typing in

        *self._username* - the user name entered

        *self._password* - the password entered

        *self._screen_size* - a rect structure that holds the dimensions of the screen, i.e. x,y,w,h

        *self._player* - the player we are dealing with, i.e. player one or player two sinces this screen is also used in two player mode

        *self._facade* - this holds a reference to the facade layer, which is a collection of helper methods.

        *self._submit_button* - this holds the position and dimensions of the submit button in a Rect 

        *self._cancel_button* - this holds the position and dimensions of the cancel button

        **public attributes**

        None


       **PUBLIC AND PRIVATE METHODS**



    """

    def __init__(self, x1, y1, w, h, dal, player = 1):
        """This is the constructor for the class:

            - parameters
            
                :param x1:      x pos of screen definition
                :param y1:      y pos of screen deinition
                :param w:       width of screen
                :param h:       height of screen
                :param dal:     a reference to the Data Access Object
                :param player:  which player the screen is for player 1 or 2
            - type of parameters
                :type x1: int
                :type y1: int
                :type w: int 
                :type h: int
                :type dal: DataAccess Object 
                :type player: int                 
            - return
                :return: none since its a constructor
            - return type
                :rtype: not applicable

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
        """
        This **public method** is the only entry point for this class.
        The display method loads and displays the screen and
        holds the gaming loop for this page.
        
        it calls the build form, processes the form i.e. allows the user to enter data
        and then validates the entered data by calling the data access layer:

            - parameters
            
                :param None:      There are no parameters for this method
                
            - return
                :return: one of Navigate enumeration values. The returned value will determine which screen we goto next.

            - return type
                :rtype: enum Navigate

        """
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
        """
        This is a **private** method that will extract the information the user has just entered
        and call a method in the *DataAccessLayer* to see if the username and password exists

            - parameters
            
                :param None:      There are no parameters for this method
                
            - return
                :return: return_value  a true or false value to signify if the login is valid or not 
            - return type
                :rtype: boolean (True or False)

        """
        return_value = False

        self._username = self._form[0].textinput.get_text()
        self._password = self._form[1].textinput.get_text()
        if self._dal.is_user_valid(self._username, self._password,self._player):
            return_value = True

        return return_value


    def _build_form(self):
        """This is a private method that builds up the form array ready for processing.
        There are no parameters and no return values since it use just class based 
        instance variables.

            - parameters
            
                :param None:      There are no parameters for this method
                
            - return
                :return: none 
            - return type
                :rtype: not applicable

        """
        self._username = pygame_textinput.TextInput('tahoma', 30, True, self._text_color, self._text_color, 400, 35)
        self._password = pygame_textinput.TextInput('tahoma', 30, True, self._text_color, self._text_color, 400, 35)
        # now create a field object for each one and add it to the forms array
        
        self._form.append(Field("username", self._username, 444, 345))
        self._form.append(Field("password", self._password, 444, 474))

        # now set the index of the form that should be input first
        self._form_index = 0


    def _process_form(self, screen, events):
        """
        This is a private method that processes the form i.e. it 
        allows the user to cycle round the list of fields we have defined by
        pressing the return key to move between fields.

            - parameters
            
                :param screen:      the screen variable to allow you to draw to it
                :param events:      a list of events

            - type of parameters
                :type screen: pygame surface object
                :type events: pygame event queue
                
            - return
                :return: none 
            - return type
                :rtype: not applicable

        """
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
