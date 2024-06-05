import pygame
import random
import settings
"""
@Author :   YANG    Lei     (S201970)
            GARDIER Simon   (S192580)

decor.py : map decoration
"""

#map representation
MAP = [
        ['┏', '━', '━', '━', '━', '━', '┳', '━', '━', '━', '━', '┳', '━', '━', '━', '━', '┳', '━', '━', '━', '━', '━', '━', '┓'],
        ['┃', ' ', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', ' ', ' ', ' ', ' ', '┃', ' ', ' ', '┃', ' ', '┗', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', ' ', '━', ' ', ' ', '┃', ' ', ' ', '┃', ' ', ' ', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', '┏', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', '↦', '━', '┫'],
        ['┃', ' ', ' ', ' ', ' ', ' ', '┗', '━', '━', '━', '━', '┛', ' ', ' ', ' ', ' ', '↥', ' ', ' ', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '━', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', '↦', '┳', '↤', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', ' ', '┃', ' ', ' ', ' ', ' ', '━', ' ', ' ', ' ', ' ', ' ', ' ', '━', '━', '━', '┛', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', ' ', '┃', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', ' ', '↥', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '↧', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', '↦', '━', '┓', ' ', ' ', ' ', ' ', '┃'],
        ['┃', ' ', '━', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ', '┃'],
        ['┗', '━', '━', '━', '━', '━', '━', '━', '━', '━', '━', '┻', '━', '━', '━', '━', '━', '━', '┻', '━', '━', '━', '━', '┛']
]
MAP_SIZE = (len(MAP[0]), len(MAP))
CASE_SIZE = settings.WINDOW_DIMENSIONS[0] / MAP_SIZE[0]

"""
Wall(Sprite) : class representing a wall
"""
class Wall(pygame.sprite.Sprite):

    # Dict containing all the possible walls
    WALL_PATHS = {
        '┃': pygame.image.load('../medias/decor/walls/vertical-wall.png'),
        '━': pygame.image.load('../medias/decor/walls/horizontal-wall.png'),
        '┓': pygame.image.load('../medias/decor/walls/top-right.png'),
        '┛': pygame.image.load('../medias/decor/walls/bottom-right.png'),
        '┏': pygame.image.load('../medias/decor/walls/top-left.png'),
        '┗': pygame.image.load('../medias/decor/walls/bottom-left.png'),
        '↤': pygame.image.load('../medias/decor/walls/horizontal-wall.png'),
        '↦': pygame.image.load('../medias/decor/walls/horizontal-wall.png'),
        '↥': pygame.image.load('../medias/decor/walls/vertical-wall.png'),
        '↧': pygame.image.load('../medias/decor/walls/vertical-wall.png'),
        '┳': pygame.image.load('../medias/decor/walls/triple-top.png'),
        '┻': pygame.image.load('../medias/decor/walls/triple-bottom.png'),
        '┫': pygame.image.load('../medias/decor/walls/triple-right.png'),
        '┣': pygame.image.load('../medias/decor/walls/triple-left.png')
    }
    def __init__(self, sprite, topleft):
        super().__init__()
        self.image = sprite.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
"""
Ground(Sprite)
"""
class Ground(pygame.sprite.Sprite):
    
    # list of random images for the floor
    GROUND_IMAGES = [
        pygame.image.load('../medias/decor/ground/ground.png'),
        pygame.image.load('../medias/decor/ground/ground1.png')
    ]
    def __init__(self, topleft):
        super().__init__()
        self.image = Ground.GROUND_IMAGES[random.randrange(2)].convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

