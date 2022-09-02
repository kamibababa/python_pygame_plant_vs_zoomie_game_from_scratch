import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, wdrect,bg_size):
        super(Bullet, self).__init__()
        self.image = pygame.image.load('material/images/Bullet_1.png').convert_alpha()
        self.rect = self.image.get_rect()

        #定义子弹的初始化位置
        self.rect.left = wdrect[0] + 45
        self.rect.top = wdrect[1]
        self.width = bg_size[0]
        self.speed = 5

    def update(self, *args):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.kill()
