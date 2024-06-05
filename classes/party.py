import pygame
import player as p
import decor
import random
import player
import board
"""
@Author :   YANG    Lei     (S201970)
            GARDIER Simon   (S192580)

Party : Game class (can be reset)
"""
class Party():

    def __init__(self, window, inParty):
        self.window = window
        #sprites
        self.ground = None
        self.walls = None
        self.players = None
        self.boards = None
        self.spells = None
        self.sprites = None
        self.inParty = inParty
        self.generated = False
        #start key
        self.party_key = pygame.K_SPACE
        self.loser = 'undefined'

    """
    play() : should be called in main loop.
    Play a game (check player state, update sprites)
    @return : True|False if party in being played
    """
    def play(self):
        for player in self.players:
            if not player.isAlive:
                self.loser = player.get_name()
                self.generated = False
                self.inParty = False
        self.sprites.update()
        self.sprites.draw(self.window)
        return self.inParty

    """
    create() : init new game
    """
    def create(self):
        self.sprites = pygame.sprite.RenderUpdates()
        """background load"""
        self.ground = pygame.sprite.RenderUpdates()
        i = 0
        for line in decor.MAP:
            j = 0
            for case in line:
                if case == ' ':
                    position    = (j * decor.CASE_SIZE, i * decor.CASE_SIZE)
                    ground_rect = pygame.Rect(position, (decor.CASE_SIZE, decor.CASE_SIZE))
                    ground      = decor.Ground(ground_rect.topleft)
                    self.ground.add(ground)
                    self.sprites.add(ground)
                j += 1
            i += 1

        """walls load"""
        self.walls = pygame.sprite.RenderUpdates()
        i = 0
        for line in decor.MAP:
            j = 0
            for case in line:
                topleft = (j * decor.CASE_SIZE, i * decor.CASE_SIZE)
                wall_rect = pygame.Rect(topleft, (decor.CASE_SIZE, decor.CASE_SIZE))
                for char, path in decor.Wall.WALL_PATHS.items():
                    if(case == char):
                        wall = decor.Wall(path, wall_rect.topleft)
                        self.walls.add(wall)
                        self.sprites.add(wall)
                j += 1
            i += 1

        """players load"""
        self.spells    = pygame.sprite.RenderUpdates()
        self.boards    = pygame.sprite.RenderUpdates()
        self.players   = pygame.sprite.RenderUpdates()

        for player_data in p.Player.PLAYERS:
            player = p.Player(player_data['name'], player_data['sprites_path'], player_data['death_sprites_path'], player_data['position'], player_data['keys'], self.walls, self.spells, self.sprites)
            self.players.add(player)
            self.sprites.add(player)
            player_board = board.PlayerBoard(player)
            self.boards.add(player_board)
            self.sprites.add(player_board)

        self.sprites.add(self.spells)
        self.inParty = True
        self.generated = True

    """
    publish()
    """
    def publish(self, keys):
        if self.inParty and self.generated:
            for player in self.players:
                player.publish(keys)