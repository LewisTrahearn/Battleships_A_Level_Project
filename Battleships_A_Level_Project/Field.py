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