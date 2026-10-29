import pygame
from core.helpers import constants
from core.helpers import assets

class MenuScene:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont(None, 48)

        # Define button rects
        btn_w, btn_h = 200, 60
        center_x = constants.GAME_WIDTH // 2 - btn_w // 2
        self.PLAY_BUTTON_RECT = pygame.Rect(center_x, 250, btn_w, btn_h)
        self.QUIT_BUTTON_RECT = pygame.Rect(center_x, 340, btn_w, btn_h)

    #From my Knowledge: Init is like a static intialization, while on_enter is called for every instance the scene is called.
    def on_enter(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
                if self.PLAY_BUTTON_RECT.collidepoint(event.pos):
                    self.game.switch("playing")
                if self.QUIT_BUTTON_RECT.collidepoint(event.pos):
                    pygame.quit()

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill(constants.MAIN_BACKGROUND_COLOR)

        # Menu Logo
        title = self.font.render("MAZE OF THE COSMOS", True, constants.PRIMARY_TEXT_COLOR)
        screen.blit(title, (constants.GAME_WIDTH // 2 - title.get_width() // 2, 150))

        # Menu Picture
        right_center_location = ((constants.LOGICAL_WIDTH-300), (constants.GAME_HEIGHT/2 - 50))
        test = assets.AssetCache.get_image("test")
        test =  pygame.transform.scale(test, (250, 250))
        screen.blit(test, right_center_location)
        # Menu Buttons
        
        pygame.draw.rect(screen, constants.GRAY, self.PLAY_BUTTON_RECT)
        pygame.draw.rect(screen, constants.GRAY, self.QUIT_BUTTON_RECT)

        play_text = self.font.render("Play", True, constants.BLACK)
        quit_text = self.font.render("Quit", True, constants.BLACK)
        screen.blit(play_text, (self.PLAY_BUTTON_RECT.centerx - play_text.get_width() // 2,
                                self.PLAY_BUTTON_RECT.centery - play_text.get_height() // 2))
        screen.blit(quit_text, (self.QUIT_BUTTON_RECT.centerx - quit_text.get_width() // 2,
                                self.QUIT_BUTTON_RECT.centery - quit_text.get_height() // 2))


