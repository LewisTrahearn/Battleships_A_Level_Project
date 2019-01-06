import pygame
from pygame.locals import *


from navigate import Navigate

import facade_layer as Facade
import optionsMenu as Menu
from optionsMenu import Button







class Options(object):
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
        self._play_button = Rect(426,656,207,58)
        self._quit_button = Rect(686,662,207,58)


    def display(self):
        """ """
        screen, background, clock = self._facade.initialise_screen("battleships", "battleship_Options_leftbar.png", self._screen_size)

        leftbar_menu = Menu.optionsMenu()
        leftbar_menu.draw(screen, Button.SIMULATION, Button.SIMULATION, self._dal)
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

            if leftbar_menu.process(pos,event,screen,self._dal) == Button.QUIT:
                return Navigate.SPLASHSCREEN            

            
            # the next statement is important otherwise carriage returns will remain and continue to be processed in the processForm           

            pygame.display.update()

            
            
            pygame.display.flip()

