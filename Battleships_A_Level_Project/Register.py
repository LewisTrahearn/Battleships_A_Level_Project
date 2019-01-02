"""
Module Name:
    Register.py

Functions/Methods:
    display

Class:
    Register
    Field

Imports:
    enum_navigate - common enumeration values shared across all classes
    facade_layer - an abstraction from the pygame module, for certain common functions
    import pygame - pygame library
    pygame.locals - this is needed for the Rect definition

Purpose:
    This class represents the Registrtation screen this is where the user can register with
    the application.
  
    
Author:
    Lewis Trahearn

"""
import pygame
from pygame.locals import *
import re


from navigate import Navigate

import facade_layer as Facade


import pygame_textinput 

class Field():
    """Container class for each field"""
    def __init__(self, fieldname, textinput, x1, y1):
        self.fieldname = fieldname
        self.textinput = textinput
        self.x1 = x1
        self.y1 = y1


class Register():
    """
    description:
    This class represents the Registrtation screen this is where the user can register with
    the application.
    
    attributes:
        _login_link             private variable that defines a screen area that is deemed to be selected.
        _register_link          private variable that defines a screen area that is deemed to be selected.
        _quit_link              private variable that defines a screen area that is deemed to be selected.
        _enum_navigate          private object that defines enumeration types for navigation
        _facade                 private object that defines the facade layer between pygame and our class
        _background             private object from pygame that represents the background 
        _yellow                 private variable, defines RGB text colour for error message
        _red                    private variable, defines RGB text colour for error message  
        _form                   private variable, defines the array that holds the form fields
        _validation_messages    private variable, an array used to hold error messages
        _form_index             private variable, keeps track of the current field in the form array 
        _text_color             private variable, defines RGB value of text and cursor for input fields 
        _username               private variable, defines the input text box 
        _password               private variable, defines the input text box  
        _forename               private variable, defines the input text box  
        _surname                private variable, defines the input text box   
        _email                  private variable, defines the input text box     
        _confirm                private variable, defines the input text box 
        _screen_size            private variable, defines the dimensions of the screen in the format (x,y,width,height) 

    methods:
        __init__(self, x1, y1, w, h)    Constructor - pass in screen size
        display                         the control loop that draws and redraws the screen
        _print_error_messages           prints any form errors
        _is_register_valid              checks form validity 
        _build_form                     builds the array of text boxes to allow the user to input.
        _process_form                   processes each text box and controls the current input.




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
        self._yellow = (250,   167,   74)
        self._red = (255,   0,   0)
        self._form = []
        self._validation_messages = []
        self._form_index = 0
        self._text_color = (22, 22, 54)
        self._username = None
        self._password = None
        self._forename = None
        self._surname  = None
        self._email    = None
        self._confirm  = None
        self._screen_size = Rect(x1, y1, w, h)

        self._facade = Facade.facade_layer()
        self._submit_button = Rect(443,904,176,47)
        self._cancel_button = Rect(683,906,187,46)


    def _create_user(self):
        return_val = True

        try:
            #taking the inputs (strings) from the text input objects
            forename = self._form[0].textinput.get_text()
            surname = self._form[1].textinput.get_text()
            username = self._form[2].textinput.get_text()
            email = self._form[3].textinput.get_text()
            password = self._form[4].textinput.get_text()
            self._dal.create_user(forename, surname, username, email, password)
            self._dal.is_user_valid(username, password)
        except:
            return_val = False
            self._validation_messages.clear()
            self._validation_messages.append("Registration failed please try again")
        
        return return_val



    def display(self):
        """ """
        screen, background, clock = self._facade.initialise_screen("battleships", "register.png", self._screen_size)

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
                        if self._is_register_valid(screen) == True:
                            if self._create_user() == True:
                                return Navigate.OPTIONS

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self._cancel_button.collidepoint(pos) == True:
                        return Navigate.SPLASHSCREEN
            
            screen.blit(background, (0, 0))
            self._print_error_messages(screen)



            
            self._process_form(screen, events)
            # the next statement is important otherwise carriage returns will remain and continue to be processed in the processForm           
            #pygame.event.clear()

            pygame.display.update()

    def _print_error_messages(self,screen):
        x = 941
        y = 549
        if len(self._validation_messages) > 0:
            self._facade.DrawStringArchivoNarrow(screen , "Reasons for form rejection" , 970, 519,self._red, False )
            for s in self._validation_messages:
                self._facade.DrawStringArchivoNarrow(screen , s , x, y,self._yellow, False )
                y = y + 30
            
            
    def _is_register_valid(self,screen):
        return_value = False

        # clears any messages from the messages array
        self._validation_messages.clear()

        #taking the inputs (strings) from the text input objects
        forename = self._form[0].textinput.get_text()
        surname = self._form[1].textinput.get_text()
        username = self._form[2].textinput.get_text()
        email = self._form[3].textinput.get_text()
        password = self._form[4].textinput.get_text()
        confirm = self._form[5].textinput.get_text()

        #this validates the length of the all the strings except email
        if len(forename) > 21:
            self._validation_messages.append("forename is more than 21 letters")
        if len(surname) > 21:
            self._validation_messages.append("surname is more than 21 letters")
        if len(username) > 21:
            self._validation_messages.append("username is more than 21 letters")
        if len(password) > 21:
            self._validation_messages.append("password is more than 21 letters")
        if len(confirm) > 21:
            self._validation_messages.append("password confirm is more than 21 letters")

        # this block of code validates the fact that something has been entered in to the input box.
        if len(forename.strip()) <= 0:
            self._validation_messages.append("you must enter a forename")
        if len(surname.strip()) <= 0:
            self._validation_messages.append("you must enter a surname")
        if len(username.strip()) <= 0:
            self._validation_messages.append("you must enter a username")
        if len(email.strip()) <= 0:
            self._validation_messages.append("you must enter an email")
        if len(password.strip()) <= 0:
            self._validation_messages.append("you must enter a password")
        if len(confirm.strip()) <= 0:
            self._validation_messages.append("you must enter a password confirmation")
        
        #This is a Regex used to check the email format is correct
        #NOTE: the Regex expression itself is taken from https://stackoverflow.com/questions/28899781/regex-for-email-according-to-wikipedia
        #I have used this because I understand that regex's are used for validation however I do not understand their complex definitions
        #I have therefore used industry standard definitions.
        check_email = re.search("^([\w\-\.]+)@((\[([0-9]{1,3}\.){3}[0-9]{1,3}\])|(([\w\-]+\.)+)([a-zA-Z]{2,4}))$", email)
        if check_email == None:
            self._validation_messages.append("invalid email format")
     
        # This is a more simple example of a Regex
        # this one starts from the beginning of the line (^)
        # it then uses a group to search for alpha characters ([a-zA-Z])
        # it then uses a plus to do this for all characters in the string (+)
        # finally it does this up until the end of line ($)
        check_forename = re.search("^[a-zA-Z]+$", forename)
        if check_forename == None:
            self._validation_messages.append("alphabet characters only in forename")
       
        #this is a repeat of the same expression above but for surname inputs.     
        check_surname = re.search("^[a-zA-Z]+$", surname)
        if check_surname == None:
            self._validation_messages.append("alphabet characters only in surname")   

        #check if there were any errors by checking if there is any messages added to the array.  
        if len(self._validation_messages) == 0:
            return_value = True
        
        #returns true or false according to wether there were any errors
        return return_value



            
            


    def _build_form(self):
        """ """
        self._username = pygame_textinput.TextInput('tahoma', 30, True, self._text_color, self._text_color, 400, 35)
        self._password = pygame_textinput.TextInput('tahoma', 30, True, self._text_color, self._text_color, 400, 35)
        self._forename = pygame_textinput.TextInput('tahoma', 30, True, self._text_color, self._text_color, 400, 35)
        self._surname  = pygame_textinput.TextInput('tahoma', 30, True, self._text_color, self._text_color, 400, 35)
        self._email    = pygame_textinput.TextInput('tahoma', 30, True, self._text_color, self._text_color, 400, 35)
        self._confirm  = pygame_textinput.TextInput('tahoma', 30, True, self._text_color, self._text_color, 400, 35)
        # now create a field object for each one and add it to the forms array
        
        self._form.append(Field("username", self._username, 429, 293))
        self._form.append(Field("password", self._password, 429, 392))
        self._form.append(Field("forename", self._forename, 429, 491))
        self._form.append(Field("surname ", self._surname , 429, 590))
        self._form.append(Field("email   ", self._email   , 429, 695))
        self._form.append(Field("confirm ", self._confirm , 429, 797))
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