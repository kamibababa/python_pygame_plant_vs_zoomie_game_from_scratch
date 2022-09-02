import pygame
import os

from Bullet import Bullet
from Peashooter import Peashooter
from SunFlower import SunFlower
from WallNut import WallNut
from Sun import Sun
from Zombie import Zombie

pygame.init()
backgd_size = (1200, 600)

screen = pygame.display.set_mode(backgd_size)
pygame.display.set_caption('plant_vs_zoomie')

bg_img_path = 'material/images/background1.jpg'
bg_img_obj = pygame.image.load(bg_img_path).convert_alpha()

# sunbank_img_path = 'material/images/SunBack.png'
# sunbank_img_obj = pygame.image.load(sunbank_img_path).convert_alpha()

sunbackImg = pygame.image.load('material/images/SeedBank.png').convert_alpha()
flower_seed = pygame.image.load("material/images/TwinSunflower.gif")
wallNut_seed = pygame.image.load("material/images/WallNut.gif")
peashooter_seed = pygame.image.load("material/images/Peashooter.gif")


text = '1000'
sun_font = pygame.font.SysFont('arial',25)
sun_num_surface = sun_font.render(text,True,(0,0,0))

peashooter = Peashooter()
# sunflower = SunFlower()
wallnut = WallNut()
zombie = Zombie()

spriteGroup = pygame.sprite.Group()
spriteGroup.add(peashooter)
# spriteGroup.add(sunflower)
spriteGroup.add(wallnut)
spriteGroup.add(zombie)

sunList = pygame.sprite.Group()

# sunList = []

clock = pygame.time.Clock()

GEN_SUN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GEN_SUN_EVENT,2000)
choose = 0
def main():
    global text
    global sun_num_surface
    running = True
    index = 0
    while running:
        # if index >= 130:
        #     index = 0

        clock.tick(20)

        #2s产生一个太阳花
        # if index % 40 == 0:
        #     sun = Sun(sunflower.rect)
        #     sunList.add(sun)

        #3s产生一个子弹
        if index % 30 == 0:
            bullet = Bullet(peashooter.rect, backgd_size)
            spriteGroup.add(bullet)


        screen.blit(bg_img_obj,(0,0))
        screen.blit(sunbackImg,(250,0))
        screen.blit(sun_num_surface,(270,60))

        screen.blit(flower_seed, (330, 10))
        screen.blit(wallNut_seed, (380, 10))
        screen.blit(peashooter_seed, (430, 10))


        spriteGroup.update(index)
        spriteGroup.draw(screen)

        sunList.update(index)
        sunList.draw(screen)

        index+=1
        for event in pygame.event.get():
            if event.type == GEN_SUN_EVENT:
                sun = Sun(sunflower.rect)
                sunList.add(sun)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_key = pygame.mouse.get_pressed()
                print(pressed_key)
                if pressed_key[0] == 1:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    x,y = pos
                    if 330<=x<=380 and 10<=y<=80 and int(text) >= 50:
                        print('点中了太阳花卡片')
                        choose = 1
                    elif 380<x<=430 and 10<=y<=80 and int(text) >= 50:
                        print('点中了坚果卡片')
                        choose = 2
                    elif 430 < x <= 480 and 10 <= y <= 80 and int(text) >= 100:
                        print('点中了豌豆射手卡片')
                        choose = 3
                    elif 250 < x < 1200 and 70<y<600:
                        print('#########')
                        print(x,y)
                        pass
                    else:
                        pass
                    for sun in sunList:
                        if sun.rect.collidepoint(pos):
                            sunList.remove(sun)
                            text = str(int(text)+50)
                            sun_font = pygame.font.SysFont('arial', 25)
                            sun_num_surface = sun_font.render(text, True, (0, 0, 0))

        pygame.display.update()

if __name__ == '__main__':
    main()
