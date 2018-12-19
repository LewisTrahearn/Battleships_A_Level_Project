"""
Module Name:
    splashscreen.py

Functions/Methods:
    display

Class:
    SplashScreen

Imports:
    enum_navigate - common enumeration values shared across all classes
    facade_layer - an abstraction from the pygame module, for certain common functions
    import pygame - pygame library
    pygame.locals - this is needed for the Rect definition

Purpose:
    This class represents the splashscreen that will introduce the user to the game
    and give them the options of either logging in, registering themselves in the game 
    or quitting.
  
    
Author:
    Lewis Trahearn

"""




import pygame
from pygame.locals import *


from navigate import Navigate

import facade_layer as Facade
from menuPointer import MenuPointer


class SplashScreen():
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



    """

    def __init__(self, x1, y1, w, h):
        """ 
        Constructor - passes dimension of screen size.

        Parameters:
        x1 - x - coord
        y1 - y - coord
        w - width
        h - height
        """

        self._screen_size = Rect(x1, y1, w, h)

        self._facade = Facade.facade_layer()

        

    def display(self):
        screen, background, clock = self._facade.initialise_screen("battleships", "splashscreen.png", self._screen_size)
        
        menu = MenuPointer()
        menu.draw(screen)
       
   

        ################################################
        # This is the main gaming loop for this screen
        ################################################
        while True:

            #cap the framerate to 30 frames per second
            clock.tick(30)

            # this loop will walk through a list of captured events
            # and react according to the specific ones we are interested in.

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return Navigate.QUIT_SPLASHSCREEN
                
                ## Get the current mouse positional information
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEMOTION:
                    menu.process(pos)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    where_next = menu.selected(pos)
                    if where_next != None:
                        return where_next


            
            
            screen.blit(background, (0, 0))
 
            menu.draw(screen)
            
            
            pygame.display.flip()


