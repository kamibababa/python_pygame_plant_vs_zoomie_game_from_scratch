import pygame
import os

WIDTH = 360
HEIGHT = 480


game_folder = os.path.dirname(__file__)
img_path = os.path.join(game_folder,'img')
player_img = pygame.image.load(os.path.join(img_path,'a.png')).convert_alpha()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        # self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
