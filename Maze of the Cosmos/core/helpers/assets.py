import pygame

#Importing Assets
class AssetCache:
    _images = {}
    _sounds = {}

    @classmethod
    def load_image(cls, key, path):
        img = pygame.image.load(path).convert_alpha()
        cls._images[key] = img

    @classmethod
    def get_image(cls, key):
        return cls._images.get(key)

    @classmethod
    def load_sound(cls, key, path):
        cls._sounds[key] = pygame.mixer.Sound(path)

    @classmethod
    def play_sound(cls, key):
        sound = cls._sounds.get(key)
        if sound:
            sound.play()