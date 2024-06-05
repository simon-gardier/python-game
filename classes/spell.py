import pygame
import math
import settings
"""
@Author :   YANG    Lei     (S201970)
            GARDIER Simon   (S192580)

Spell(Sprite)
"""

class Spell(pygame.sprite.Sprite):

    MOVEMENT_SIZE = 12
    SPELL = pygame.image.load('../medias/spell/spell.png')
    def __init__(self, pos, orientation, inaccessible_group, all_sprites_group):
        super().__init__()
        self.orientation = orientation
        self.orientation_radian = ((math.pi) / 180) * orientation
        self.image = pygame.transform.rotate(Spell.SPELL, self.orientation)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.inaccessible_group = inaccessible_group
        self.all_sprites_group = all_sprites_group
        self.fps = settings.FPS
    
    """
    update() : Update spell state, if spell touches an obstacle, an animation is played, then the spell destroyed
    """
    def update(self):
        previous_position   = self.get_position()
        new_position        = (self.rect.center[0] + Spell.MOVEMENT_SIZE * math.cos(self.orientation_radian), self.rect.center[1] + Spell.MOVEMENT_SIZE * -math.sin(self.orientation_radian))
        self.set_position(new_position)
        for obstacle in self.inaccessible_group:
            if pygame.Rect.colliderect(obstacle.rect, self.rect):
                self.set_position(previous_position)
                self.hit_animation(obstacle.rect)
                self.kill()

    """
    hit_animation() : creates a hit animation and add the image to the sprites group to draw
    @param - obstacle : rectangle with whom the spell collided
    """
    def hit_animation(self, obstacle):
        orientation = 0
        if obstacle.right < self.rect.left:
            orientation = 0
        elif obstacle.bottom < self.rect.top:
            orientation = 270
        elif obstacle.left > self.rect.right:
            orientation = 180
        elif obstacle.top > self.rect.bottom:
            orientation = 90
        self.all_sprites_group.add(HitAnimation(orientation, self.rect.topleft))

    """
    Getters/Setters
    """
    def get_position(self):
        return self.rect.center
    
    def set_position(self, center_position):
        self.rect.center = center_position
        self.image = pygame.transform.rotate(Spell.SPELL, self.orientation)

"""
HitAnimation(Sprite)
"""
class HitAnimation(pygame.sprite.Sprite):
    #animation images
    HIT_ANIMATION = [
        pygame.image.load('../medias/spell/hit_animation/1.png'),
        pygame.image.load('../medias/spell/hit_animation/2.png'),
        pygame.image.load('../medias/spell/hit_animation/3.png'),
        pygame.image.load('../medias/spell/hit_animation/4.png')
    ]

    HIT_DURATION = settings.FPS / 5
    
    def __init__(self, orientation, pos):
        super().__init__()
        self.orientation = orientation
        self.image = pygame.transform.rotate(HitAnimation.HIT_ANIMATION[0], self.orientation)
        self.rect = self.image.get_rect(topleft = pos)
        self.current_animation_duration = 0
    
    """
    update()
    """
    def update(self):
        if self.current_animation_duration <= HitAnimation.HIT_DURATION:
            currentArrayAnimationPosition = self.current_animation_duration / HitAnimation.HIT_DURATION * len(HitAnimation.HIT_ANIMATION) - 1
            self.image = pygame.transform.rotate(HitAnimation.HIT_ANIMATION[int(currentArrayAnimationPosition)], self.orientation)
            self.current_animation_duration += 1
        else:
            self.kill()