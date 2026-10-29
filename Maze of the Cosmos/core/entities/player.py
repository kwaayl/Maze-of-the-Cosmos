import pygame
from core.helpers import constants
from core.helpers import assets

class Player:
    def __init__(self, grid_x, grid_y):
        self.grid_x = grid_x 
        self.grid_y = grid_y

    def move(self, dx, dy):
        new_x = self.grid_x + dx
        new_y = self.grid_y + dy

        #Checker to stay in game
        if 0 <= new_x < constants.GRID_SIZE and 0 <= new_y < constants.GRID_SIZE:
            self.grid_x = new_x
            self.grid_y = new_y

    def get_pixel_pos(self):
        # converts grid position to pixel position on screen
        x = constants.GRID_AREA_X + self.grid_x * constants.CELL_SIZE_WIDTH
        y = self.grid_y * constants.CELL_SIZE_HEIGHT
        return x, y

    def draw(self, screen):
        x, y = self.get_pixel_pos()
        #cat = assets.AssetCache.get_image("catPlayer").convert_alpha()
        boss = assets.AssetCache.get_image("bossJas").convert_alpha()
        
        rect = pygame.Rect(x + 10, y + 10, constants.CELL_SIZE_WIDTH - 20, constants.CELL_SIZE_HEIGHT - 20)
        # pygame.draw.rect(screen, constants.PLAYER_COLOR, rect, border_radius=8)
        cat_scaled = pygame.transform.scale(boss, (rect.width, rect.height))
        screen.blit(cat_scaled, rect)