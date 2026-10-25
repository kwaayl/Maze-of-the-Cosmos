# Engine Basically
import pygame
from core.helpers import constants
from core.scenes import menu
from core.scenes import playing

class Game:
    #Initialization
    def __init__(self):
        self.screen = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT), pygame.RESIZABLE)
        self.logical_surface = pygame.Surface((constants.LOGICAL_WIDTH, constants.LOGICAL_HEIGHT))
        self.clock = pygame.time.Clock()
        self.scenes = {}
        self.current_scene = None
        self.fullscreen = False

        #Registering Scenes
        self.register("menu", menu.MenuScene(self))
        self.register("playing", playing.PlayingScene(self))

        #Enter First Scene (Menu) First
        self.switch("menu")
        
    #SceneCreation Logic
    def register(self, name, scene):
        self.scenes[name] = scene

    #SceneSwitching Logic
    def switch(self, name):
        self.current_scene = self.scenes[name]
        self.current_scene.on_enter()

    #Taking Delta Time for Event Handling
    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                self._handle_global_event(event)
                self.current_scene.handle_event(event)
            self.current_scene.update(dt)
            self.current_scene.draw(self.logical_surface)
            self._render()

    #Rendering a Scaling Constant
    def _render(self):
        windowed_w, windowed_h = self.screen.get_size()
        scale = min(windowed_w / constants.LOGICAL_WIDTH, windowed_h / constants.LOGICAL_HEIGHT)
        scaled_w = int(constants.LOGICAL_WIDTH * scale)
        scaled_h = int(constants.LOGICAL_HEIGHT * scale)
        scaled = pygame.transform.scale(self.logical_surface, (scaled_w, scaled_h))
        offset_x = (windowed_w - scaled_w) // 2
        offset_y = (windowed_h - scaled_h) // 2
        self.screen.fill((0, 0, 0))
        self.screen.blit(scaled, (offset_x, offset_y))
        pygame.display.flip()

    #Insert Keybind Logic Here: The only Case is for Fullscreen because it needs to be constantly during runtime.
    def _handle_global_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    self.window = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT), pygame.RESIZABLE)