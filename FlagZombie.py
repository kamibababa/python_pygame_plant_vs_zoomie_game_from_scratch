import random
import pygame

from Zombie import Zombie


class FlagZombie(Zombie):
    def __init__(self):
        super(FlagZombie,self).__init__()
        self.image = pygame.image.load('material/images/FlagZombie_0.png').convert_alpha()
        self.images = [pygame.image.load('material/images/FlagZombie_{}.png'.format(i)).convert_alpha() for i in range(0,12)]

        # self.rect = self.images[0].get_rect()
        # self.rect.top = 25 + random.randrange(0,4)*125
        self.energy = 10
        # self.rect.left = 1000
        self.speed = 4

    # def update(self, *args):
    #     if self.energy > 0:
    #         self.image = self.images[args[0] % len(self.images)]
    #         if self.rect.left > 250:
    #             self.rect.left -= self.speed
    #     else:
    #         self.kill()
