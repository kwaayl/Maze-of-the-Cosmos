# core/scenes/playing.py
import pygame
from core.helpers import constants
from core.entities import player

#TO DO: Build level loading logic and a level builder
#TO DO: Build Mouse Handling for Moving Tiles
#TO DO: Build Spacebar to spend a move (?) unsure
class PlayingScene:
    def __init__(self, game):
        self.game = game
        self.player = player.Player(0, 0)

    def on_enter(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.player.move(0, -1)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.player.move(0, 1)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.player.move(-1, 0)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.player.move(1, 0)

    def update(self, dt):
        pass

    def draw(self, screen):
        self._draw_sidebar(screen)
        self._draw_grid(screen)
        self.player.draw(screen)

    #Sidebar Logic
    def _draw_sidebar(self, screen):
        SIDEBAR_RECT = pygame.Rect(0, 0, constants.SIDEBAR_WIDTH, constants.LOGICAL_HEIGHT)
        pygame.draw.rect(screen, constants.SIDEBAR_BACKGROUND_COLOR, SIDEBAR_RECT)

    #Playable Field Grid Logic
    def _draw_grid(self, screen):
        # Grid background
        GRID_RECT = pygame.Rect(constants.GRID_AREA_X, 0, constants.GRID_AREA_WIDTH, constants.GRID_AREA_HEIGHT)
        pygame.draw.rect(screen, constants.GRID_BACKGROUND_COLOR, GRID_RECT)

        # Build Grid lines
        for row in range(constants.GRID_SIZE + 1):
            y = row * constants.CELL_SIZE_HEIGHT
            pygame.draw.line(screen, constants.GRID_INSET_LINE_COLOR, (constants.GRID_AREA_X, y), (constants.LOGICAL_WIDTH, y), 1)

        for col in range(constants.GRID_SIZE + 1):
            x = constants.GRID_AREA_X + col * constants.CELL_SIZE_WIDTH
            pygame.draw.line(screen, constants.GRID_INSET_LINE_COLOR, (x, 0), (x, constants.GRID_AREA_HEIGHT), 1)