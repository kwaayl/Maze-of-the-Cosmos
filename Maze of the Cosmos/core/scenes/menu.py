import pygame
from core.helpers import constants

class MenuScene:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont(None, 48)

        # Define button rects
        btn_w, btn_h = 200, 60
        center_x = constants.GAME_WIDTH // 2 - btn_w // 2
        self.play_rect = pygame.Rect(center_x, 250, btn_w, btn_h)
        self.quit_rect = pygame.Rect(center_x, 340, btn_w, btn_h)

    #From my Knowledge: Init is like a static intialization, while on_enter is called for every instance the scene is called.
    def on_enter(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_rect.collidepoint(event.pos):
                    self.game.switch("puzzle")
                if self.quit_rect.collidepoint(event.pos):
                    pygame.quit()

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill(constants.MAIN_BACKGROUND_COLOR)

        # Menu Logo
        title = self.font.render("MAZE OF THE COSMOS", True, constants.PRIMARY_TEXT_COLOR)
        screen.blit(title, (constants.GAME_WIDTH // 2 - title.get_width() // 2, 150))

        # Menu Picture

        # Menu Buttons
        
        pygame.draw.rect(screen, constants.GRAY, self.play_rect)
        pygame.draw.rect(screen, constants.GRAY, self.quit_rect)

        play_text = self.font.render("Play", True, constants.BLACK)
        quit_text = self.font.render("Quit", True, constants.BLACK)
        screen.blit(play_text, (self.play_rect.centerx - play_text.get_width() // 2,
                                self.play_rect.centery - play_text.get_height() // 2))
        screen.blit(quit_text, (self.quit_rect.centerx - quit_text.get_width() // 2,
                                self.quit_rect.centery - quit_text.get_height() // 2))


