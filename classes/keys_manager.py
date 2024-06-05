import pygame
import sys
"""
@Author :   YANG    Lei     (S201970)
            GARDIER Simon   (S192580)

KeysManager : check which keys are pressed and publish it
"""
class KeysManager():

    def __init__(self, subscribers, keys_map):
        self.subscribers = subscribers
        self.keys_map = keys_map

    """
    manage_keys() : updates self.keys_map
    """
    def manage_keys(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evenement.type == pygame.KEYDOWN:
                if evenement.key in self.keys_map:
                    self.keys_map[evenement.key] = True
            if evenement.type == pygame.KEYUP:
                if evenement.key in self.keys_map:
                    self.keys_map[evenement.key] = False
        self.publish()

    """
    publish()
    """
    def publish(self):
        for subscriber in self.subscribers:
            subscriber.publish(self.keys_map)
