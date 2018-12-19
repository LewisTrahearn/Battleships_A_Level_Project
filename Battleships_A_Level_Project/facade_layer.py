"""
Module Name:
    facade_layer.py

Functions/Methods:


Class:
    facade_layer - simpler interface to the pygame library.

Imports:
    random - allow the generation of random numbers
    os.path - specifically load the namespace os.path so that I can retrieve information about the directory path
    pygame - this is the main game library (https://www.pygame.org/news)

Purpose:
    a facade layer is a design pattern within UML (Unified Modelling Language) that allows you to put a simpler
    interface in place for a group of classes.

    In our case the interface I am trying to simplify is a layer between my game logic
    and the pygame library, so where possible I shall put in here common methods
    that are reusable within the battleships game.

    This may not be possible for all things, however it will help simply the game logic.
    
Author:
    Lewis Trahearn

"""

import os.path
import pygame
from pygame.locals import *


class facade_layer(object):
    """
    description:
    a facade layer is a design pattern within UML (Unified Modelling Language) that allows you to put a simpler
    interface in place for a group of classes.

    In our case the interface I am trying to simplify is a layer between my game logic
    and the pygame library, so where possible I shall put in here common methods
    that are reusable within the battleships game.

    This may not be possible for all things, however it will help simply the game logic.
    
    attributes:
        name - this is used as a control variable to stop the sounds and music from repeating

    methods:
        __init__(self) - default constructor no parameters required
        loadImage(self,file) - public method to load an image
        DrawString(self,screen, background, s, x, y, fg, bg, font, size, bold) - public method to draw a string of characters to the screen using a system font
        DrawStringPirateFont(self,screen, s, x, y, fg, bg  ) - public method to draw a string to the screen using a pirate font
        DrawStringArchivoNarrow(self,screen, s, x, y, fg, bg  ) public method to draw to the screen using Archivo Narrow font
        playRolloverSound(self,name): - public method to play roll over sound 
        playLaunchSound(self,name) - public method, plys lauch sound of missile
        playExplosionWithSplashSound(self,name) - public method, plays an explosion with a splash sound for a miss
        DrawName(self,screen, s, x, y, fg, bg  ) - used to draw a user name on the screen
        DrawGameOver(self,screen, s, x, y, fg, bg  ) - used to draw the game over message

    """
    def __init__(self):
        self.name = ""

    def initialise_screen(self, title, image_name, screen_size_rect):
        pygame.init()

        pygame.display.set_caption(title)
        pygame.mouse.set_visible(1)

        if pygame.mixer and not pygame.mixer.get_init():
            print ('Warning, no sound')
            pygame.mixer = None

        # Set the display mode
        winstyle = 0  # |FULLSCREEN
        bestdepth = pygame.display.mode_ok(screen_size_rect.size, winstyle, 32)
        screen = pygame.display.set_mode(screen_size_rect.size, winstyle, bestdepth)

        background = self.loadImage(image_name)
        screen.blit(background, (0,0))
        pygame.display.flip()
        clock = pygame.time.Clock()
        return screen, background, clock

    def loadImage(self,file):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, 'images', file)
        try:
            surface = pygame.image.load(file)
        except pygame.error:
            raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
        return surface.convert_alpha()  

    def DrawString(self,screen, background, s, x, y, fg, bg, font, size, bold):
        verdana = pygame.font.match_font(font)
        
        verdanaFont = pygame.font.Font(verdana, size)
        verdanaFont.set_bold(bold)

        #font = pygame.font.Font(font,size)
        #font.set_bold(True)
        textImg = verdanaFont.render(s,1,fg, bg)
        background.blit( textImg, (x,y) )
        background.set_alpha(0)
        screen.blit(background, (0,0))
        pygame.display.flip()   

    def DrawStringPirateFont(self,screen, s, x, y, fg, bg  ):

        
        file = "PirataOne-Regular.ttf"
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, 'fonts', file)

        font = pygame.font.Font(file, 125)
        #font.set_bold(True)

        textImg = font.render(s,1,fg, bg).convert_alpha(screen)
        textImgRect = textImg.get_rect()
        textImgRect.x = x
        textImgRect.y = y
        
        screen.blit( textImg, textImgRect)

    def DrawStringArchivoNarrow(self,screen, s, x, y, fg, bg  ):

        
        file = "ArchivoNarrow-Regular.ttf"
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, 'fonts', file)

        font = pygame.font.Font(file, 21)
        #font.set_bold(True)

        textImg = font.render(s,1,fg, bg).convert_alpha(screen)
        textImgRect = textImg.get_rect()
        textImgRect.x = x
        textImgRect.y = y
        
        screen.blit( textImg, textImgRect) 

    def playRolloverSound(self,name):
        if pygame.mixer:
            if self.name != name:
                main_dir = os.path.split(os.path.abspath(__file__))[0]
                music = os.path.join(main_dir, 'sound', 'rollover.mp3')
                pygame.mixer.music.load(music)
                pygame.mixer.music.play(1)
                self.name = name

    def playLaunchSound(self,name):
        if pygame.mixer:
            main_dir = os.path.split(os.path.abspath(__file__))[0]
            music = os.path.join(main_dir, 'sound', 'Missile+1.mp3')
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(1)

        
    def playExplosionWithSplashSound(self,name):
        if pygame.mixer:
            main_dir = os.path.split(os.path.abspath(__file__))[0]
            music = os.path.join(main_dir, 'sound', 'ExplosionWithSplash.mp3')
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(1)

    def DrawName(self,screen, s, x, y, fg, bg  ):

        
        file = "ArchivoNarrow-Bold.ttf"
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, 'fonts', file)

        font = pygame.font.Font(file, 32)
        #font.set_bold(True)

        textImg = font.render(s,1,fg, bg).convert_alpha(screen)
        textImgRect = textImg.get_rect()
        centerText = 202 - textImgRect.width
        if centerText <= 0:
            centerText = 0
        textImgRect.x = x + centerText/2
        textImgRect.y = y
        
        screen.blit( textImg, textImgRect) 

    def DrawGameOver(self,screen, s, x, y, fg, bg  ):

        #screenSize = rect(0,0,1280,1024)

        file = "PirataOne-Regular.ttf"
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, 'fonts', file)

        font = pygame.font.Font(file, 125)
        #font.set_bold(True)

        textImg = font.render(s,1,fg, bg).convert_alpha(screen)
        textImgRect = textImg.get_rect()
        centerText = 1280 - textImgRect.width
        if centerText <= 0:
            centerText = 0
        textImgRect.x = x + centerText/2
        textImgRect.y = y
        
        screen.blit( textImg, textImgRect)
