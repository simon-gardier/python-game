import pygame
import menu
import party
import player
import keys_manager
"""
@Author :   YANG    Lei     (S201970)
            GARDIER Simon   (S192580)

Game() : handle games logic
        - players objects
        - menus
        - game itself
        - keyboard + window
"""

class Game():

    def __init__(self, window, fps, clock, title):
        self.window = window
        self.window_size = self.window.get_size()
        self.FPS = fps
        self.clock = clock
        self.inGame = True
        self.quit_key = pygame.K_ESCAPE
        self.menu = menu.Menu(self.window_size, self.window, title, True)
        self.end_menu = menu.EndMenu(self.window_size, self.window, False)
        self.party = party.Party(self.window, False)
        self.keys_map = {
            self.party.party_key : False,
            self.menu.menu_key : False,
            self.quit_key : False
        }
        self.keys_map.update(player.Player.all_players_keys)
        self.subscribers = [self, self.party]
        self.keys_manager = keys_manager.KeysManager(self.subscribers, self.keys_map)

    """
    loop() : main loop called in main.py
    """
    def loop(self):
        while self.inGame:
            #registers pressed keys and publish to subs
            self.keys_manager.manage_keys()
            if self.menu.inMenu:
                self.menu.draw()
            if self.party.inParty:
                if self.party.generated:
                    if not self.party.play():
                        self.end_menu.inEndMenu = True
                else:
                    self.party.create()
            if self.end_menu.inEndMenu:
                self.end_menu.set_loser(self.party.loser)
                self.end_menu.draw()

            pygame.display.flip()
            self.clock.tick(self.FPS)
    
    """
    publish(keys) : publish pressed keyts
    @param keys values (True|False)
    """
    def publish(self, keys):
        # leaves program
        if keys[self.quit_key]:
            self.inGame = False
        if self.end_menu.inEndMenu:
            # if player wnats to come back to main menu
            if keys[self.menu.menu_key]:
                self.end_menu.inEndMenu = False
                self.end_menu.death_message = None
                self.menu.inMenu = True
        if self.menu.inMenu:
            # if player wants to start new game
            if keys[self.party.party_key]:
                self.menu.inMenu = False
                self.party.inParty = True
