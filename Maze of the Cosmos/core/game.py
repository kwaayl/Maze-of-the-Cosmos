# Engine Basically
import pygame
from core.helpers import constants
from core.scenes import menu
from core.scenes import playing

class Game:
    #Initialization
    def __init__(self):
        self.screen = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))
        self.clock = pygame.time.Clock()
        self.scenes = {}
        self.current_scene = None

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
                self.current_scene.handle_event(event)
            self.current_scene.update(dt)
            self.current_scene.draw(self.screen)
            pygame.display.flip()