import pygame
import random
"""
@Author :   YANG    Lei     (S201970)
            GARDIER Simon   (S192580)

menu.py : Handles menus
"""

"""
Menu : Start menu
"""
class Menu():

    #menu medias
    DUNGEON_IMAGE   = pygame.image.load('../medias/menu/menu_background.jpg')
    KEYBOARD_IMAGE  = pygame.image.load('../medias/menu/keyboard.png')
    paragraph_font  = pygame.font.Font('../medias/retro_font.ttf', 32)
    title_font      = pygame.font.Font('../medias/retro_font.ttf', 48)

    def __init__(self, window_size, window, title, inMenu):
        self.window_size = window_size
        self.window = window
        self.paragraph_font = Menu.paragraph_font
        self.title_font = Menu.title_font
        self.title = title
        self.background_image = Menu.DUNGEON_IMAGE
        self.KEYBOARD_IMAGE = Menu.KEYBOARD_IMAGE
        # used in party.py > Party to know what to display
        self.inMenu = inMenu
        # key to display menu
        self.menu_key = pygame.K_m

    """
    draw() : draw menu
    """
    def draw(self):
        #background
        background = self.background_image
        background_rect = pygame.rect.Rect((0, 0), background.get_size())
        self.window.blit(background, background_rect)
        #title
        title = self.title_font.render(self.title, True, (255, 255, 255))
        title_size = title.get_size()
        title_position = (self.window_size[0]//2 - title_size[0]//2, 100)
        title_rect = pygame.rect.Rect(title_position, title_size)
        self.window.blit(title, title_rect)                                                                                                          
        #background bottom
        bottom_background = pygame.surface.Surface((self.window_size[0], 200))
        bottom_background.fill((0, 0, 0))
        bottom_background_size = bottom_background.get_size()
        bottom_background_position = (0, self.window_size[1] - bottom_background_size[1])
        bottom_background_rect = pygame.rect.Rect(bottom_background_position, bottom_background_size)
        self.window.blit(bottom_background, bottom_background_rect)
        #images 
        keyboard = self.KEYBOARD_IMAGE
        keyboard_size = keyboard.get_size()
        margin = bottom_background_size[1]//2 - keyboard_size[1]//2
        keyboard_position = (margin, bottom_background_rect[1] + margin)
        keyboard_rect = pygame.rect.Rect(keyboard_position, keyboard_size)
        self.window.blit(keyboard, keyboard_rect)
        #tips and legends
        first_line = self.paragraph_font.render('<- Keyboard layout', True, (255, 255, 255))
        first_line_size = first_line.get_size()
        first_line_position = (keyboard_rect.topright[0] + 15, keyboard_position[1])
        first_line_rect = pygame.rect.Rect(first_line_position, first_line_size)
        self.window.blit(first_line, first_line_rect)

        tips = self.paragraph_font.render("Press (espace) to play", True, (255, 255, 255))
        tips_size = tips.get_size()
        tips_position = ( keyboard_rect.topright[0] + 15, first_line_rect.bottom +  + 10)
        tips_rect = pygame.rect.Rect(tips_position, tips_size)
        self.window.blit(tips, tips_rect)

        tips1 = self.paragraph_font.render("Press (esc) to quit", True, (255, 255, 255))
        tips1_size = tips1.get_size()
        tips1_position = ( tips_position[0], tips_rect.bottom+ 10)
        tips1_rect = pygame.rect.Rect(tips1_position, tips1_size)
        self.window.blit(tips1, tips1_rect)

"""
EndMenu : End game menu
"""
class EndMenu():
    #menu medias
    skull_image = pygame.image.load('../medias/menu/skull.png')
    paragraph_font  = pygame.font.Font('../medias/retro_font.ttf', 32)
    title_font      = pygame.font.Font('../medias/retro_font.ttf', 32)
    #random death sentece
    phrases = [
        ' was destroyed',
        ' prefered to resign',
        ' found better than them',
        ' was not focus',
        ' should question themselves',
        ' forgot how to play'
    ]

    def __init__(self, window_size, window, inEndMenu):
        self.window_size = window_size
        self.window = window
        #loser name
        self.loser = 'undefined'
        self.inEndMenu = inEndMenu
        self.title_font = EndMenu.title_font
        self.paragraph_font = EndMenu.paragraph_font
        self.skull_image = EndMenu.skull_image
        self.death_message = None

    """
    draw() : draw end game menu
    """
    def draw(self):
        #background
        self.window.fill((0, 0, 0))
        if self.death_message == None:
            self.death_message = self.choose_death_message()
        #death message
        first_line = self.title_font.render(self.loser + self.death_message, True, (255, 255, 255))
        first_line_size = first_line.get_size()
        #image
        emote_image = self.skull_image
        emote_image_size = emote_image.get_size()
        first_line_rect = pygame.rect.Rect((self.window_size[0]//2 - first_line_size[0]//2 - emote_image_size[0]//2, self.window_size[1]//2 - first_line_size[1]//2), first_line_size)
        emote_image_rect = pygame.rect.Rect((first_line_rect.right + 10, first_line_rect.centery - emote_image_size[1]//2), emote_image_size)
        self.window.blit(first_line, first_line_rect)
        self.window.blit(emote_image, emote_image_rect)
        #Tips
        second_line      = self.paragraph_font.render('Press (esc) to quit', True, (255, 255, 255)) 
        second_line_size = second_line.get_size()
        second_line_rect = pygame.rect.Rect((self.window_size[0]//2 - second_line_size[0]//2, first_line_rect.top+90), second_line_size)
        self.window.blit(second_line, second_line_rect)

        third_line      = self.paragraph_font.render('Press (m) for main meny', True, (255, 255, 255)) 
        third_line_size = third_line.get_size()
        third_line_rect = pygame.rect.Rect((self.window_size[0]//2 - third_line_size[0]//2, second_line_rect.top+50), third_line_size)
        self.window.blit(third_line, third_line_rect)

    """
    choose_death_message() : choose random sentence
    @return : string - Chosen sentence
    """
    def choose_death_message(self):
        return EndMenu.phrases[random.randrange(0, len(EndMenu.phrases) - 1)]

    """
    set_loser(loser) : setter for loser
    """
    def set_loser(self, loser):
        self.loser = loser
