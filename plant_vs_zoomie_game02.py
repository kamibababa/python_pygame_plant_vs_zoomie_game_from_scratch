
import pygame
import os
WIDTH = 360
HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('plant_vs_zoomie')




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



# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# myfont = pygame.font.Font(None,60)
# textImgage = myfont.render('pygame',True,WHITE)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)



FPS = 60
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
