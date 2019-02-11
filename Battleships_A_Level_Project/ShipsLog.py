


import pygame
from pygame.locals import *


from navigate import Navigate

import facade_layer as Facade
import optionsMenu as Menu
import Board as Board
import Allocation as Allocation
import player as Player
import ComputerPlayer as CPU
import ShipsLogMenu as Menu
import StatsContainer as StatsCon
from  ShipsLogMenu import MenuOptionButton



class ShipsLog(object):
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

        # MORE CONSTANTS
        self.YELLOW = (250,   167,   74)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)


    def display_table_hits(self, results, screen):
        counter = 0
        x = 712
        x1 = 1134
        y= 343

        self._facade.DrawStringArchivoNarrow(screen,"Rank", 408, 264,self.WHITE, False, 34 )
        self._facade.DrawStringArchivoNarrow(screen,"Player", 767, 264,self.WHITE, False, 34 )
        self._facade.DrawStringArchivoNarrow(screen,"Hits", 1134, 264,self.WHITE, False, 34 )

        for stat in results:
            if counter >= 10:
                break;
            self._facade.DrawStringArchivoNarrow(screen,stat.username, x, y,self.WHITE, False, 34 )
            self._facade.DrawStringArchivoNarrow(screen,str(stat.number_of_shots), x1, y,self.WHITE, False, 34 )
            y = y + 50
            counter = counter + 1

    def display_table_least_time(self, results, screen):
        counter = 0
        x = 712
        x1 = 1077
        y= 343

        self._facade.DrawStringArchivoNarrow(screen,"Rank", 408, 264,self.WHITE, False, 34 )
        self._facade.DrawStringArchivoNarrow(screen,"Player", 767, 264,self.WHITE, False, 34 )
        self._facade.DrawStringArchivoNarrow(screen,"Time", 1134, 264,self.WHITE, False, 34 )

        for stat in results:
            if counter >= 10:
                break;
            self._facade.DrawStringArchivoNarrow(screen,stat.username, x, y,self.WHITE, False, 34 )
            self._facade.DrawStringArchivoNarrow(screen,str(stat.gametime), x1, y,self.WHITE, False, 34 )
            y = y + 50
            counter = counter + 1

    def display_table_most_wins(self, results, screen):
        counter = 0
        x = 712
        x1 = 1077
        y= 343

        self._facade.DrawStringArchivoNarrow(screen,"Rank", 408, 264,self.WHITE, False, 34 )
        self._facade.DrawStringArchivoNarrow(screen,"Player", 767, 264,self.WHITE, False, 34 )
        self._facade.DrawStringArchivoNarrow(screen,"Most Wins", 1134, 264,self.WHITE, False, 34 )

        for stat in results:
            if counter >= 10:
                break;
            self._facade.DrawStringArchivoNarrow(screen,stat.username, x, y,self.WHITE, False, 34 )
            self._facade.DrawStringArchivoNarrow(screen,str(stat.win_count), x1, y,self.WHITE, False, 34 )
            y = y + 50
            counter = counter + 1

    def display_profile(self,gamecount,  win_count,  lowest_number_of_hits, bestTime, screen):
        self._facade.DrawStringArchivoNarrow(screen,str(gamecount), 705, 360,self.WHITE, False, 34 )
        self._facade.DrawStringArchivoNarrow(screen,str(win_count), 705, 425,self.WHITE, False, 34 )
        self._facade.DrawStringArchivoNarrow(screen,bestTime, 705, 490,self.WHITE, False, 34 )
        self._facade.DrawStringArchivoNarrow(screen,str(lowest_number_of_hits), 705, 569,self.WHITE, False, 34 )

        position_based_on_hits = self._dal.get_position_in_crew_based_upon_shots(lowest_number_of_hits)
        self._facade.DrawStringArchivoNarrow(screen,position_based_on_hits, 955, 569,self.WHITE, False, 34 )

        position_based_upon_time = self._dal.get_position_in_crew_based_upon_gametime(bestTime)
        self._facade.DrawStringArchivoNarrow(screen,position_based_upon_time, 955, 490,self.WHITE, False, 34 )


    def display(self):
        """ """
        screen, background, clock = self._facade.initialise_screen("battleships", "shipsLog_background.png", self._screen_size)

        menu = Menu.ShipsLogMenu(screen, self._dal)
        self._dal.load_game_stats()
        self._dal.load_number_of_games_stats()

        results = self._dal.sort_by_number_of_shots()
        gametime_results = self._dal.sort_by_gametime()
        number_of_wins_results = self._dal.sort_by_number_of_wins()

        gamecount,  win_count,  lowest_number_of_hits, bestTime = self._dal.get_logged_in_player_1_stats()

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

            menu.process(pos, event) 
            if menu.getCurrentSelected() == MenuOptionButton.LEAST_HITS:
                self.display_table_hits(results, screen)

            if menu.getCurrentSelected() == MenuOptionButton.LEAST_TIME:
                self.display_table_least_time(gametime_results, screen)

            if menu.getCurrentSelected() == MenuOptionButton.MOST_WINS:
                self.display_table_most_wins(number_of_wins_results, screen)
            
            if menu.getCurrentSelected() == MenuOptionButton.YOUR_PROFILE:
                self.display_profile(gamecount,  win_count,  lowest_number_of_hits, bestTime, screen)

            if menu.getCurrentSelected() == MenuOptionButton.EXIT:
                    return Navigate.SPLASHSCREEN            

            # the next statement is important otherwise carriage returns will remain and continue to be processed in the processForm           

            pygame.display.update()
         
            







