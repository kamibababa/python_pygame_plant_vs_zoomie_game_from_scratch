import pygame

class WallNut(pygame.sprite.Sprite):
    def __init__(self):
        super(WallNut, self).__init__()
        self.image = pygame.image.load('material/images/WallNut_00.png').convert_alpha()
        self.images = [pygame.image.load('material/images/WallNut_{:02d}.png'.format(i)).convert_alpha() for i in range(0,13)]
        self.crackedImgs = [
            pygame.transform.smoothscale(pygame.image.load("material/images/Wallnut_body.png").convert_alpha(),
                                         (self.image.get_rect().width, self.image.get_rect().height)),
            pygame.transform.smoothscale(
                pygame.image.load("material/images/Wallnut_cracked1.png").convert_alpha(),
                (self.image.get_rect().width, self.image.get_rect().height)),
            pygame.transform.smoothscale(
                pygame.image.load("material/images/Wallnut_cracked2.png").convert_alpha(),
                (self.image.get_rect().width, self.image.get_rect().height))]
        self.rect = self.images[0].get_rect()
        self.rect.top = 200
        self.rect.left = 250

        self.energy = 8*15
        self.zombies = set()

    def update(self, *args):
        for zombie in self.zombies:
            if zombie.isAlive == False:
                continue

            self.energy -= 1

        if self.energy <= 0:
            for zombie in self.zombies:
                zombie.isMeetWallNut = False
            self.kill()


        if self.energy == 8*15:
            self.image = self.images[args[0] % len(self.images)]
        elif 6*15 <= self.energy < 8*15:
            self.image = self.crackedImgs[0]
        elif 3 * 15 <= self.energy < 6 * 15:
            self.image = self.crackedImgs[1]
        else:
            self.image = self.crackedImgs[2]
