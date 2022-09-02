import random

import pygame

class Sun(pygame.sprite.Sprite):
    def __init__(self,rect):
        super(Sun,self).__init__()
        self.image = pygame.image.load('material/images/Sun_1.png').convert_alpha()
        self.images = [pygame.image.load('material/images/Sun_{}.png'.format(i)).convert_alpha() for i in range(1,18)]

        self.rect = self.images[0].get_rect()

        offsetTop = random.randint(-50,50)
        offsetLeft = random.randint(-50,50)

        self.rect.top = rect.top + offsetTop
        self.rect.left = rect.left + offsetLeft

    def update(self, *args):


        self.image = self.images[args[0] % len(self.images)]

