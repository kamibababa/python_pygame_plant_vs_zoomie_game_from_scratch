import pygame
import os
from Peashooter import Peashooter
from SunFlower import SunFlower
from WallNut import WallNut
from Sun import Sun

pygame.init()
backgd_size = (1200, 600)

screen = pygame.display.set_mode(backgd_size)
pygame.display.set_caption('plant_vs_zoomie')

bg_img_path = 'material/images/background1.jpg'
bg_img_obj = pygame.image.load(bg_img_path).convert_alpha()

sunbank_img_path = 'material/images/SunBack.png'
sunbank_img_obj = pygame.image.load(sunbank_img_path).convert_alpha()

text = '900'
sun_font = pygame.font.SysFont('arial',25)
sun_num_surface = sun_font.render(text,True,(0,0,0))

peashooter = Peashooter()
sunflower = SunFlower()
wallnut = WallNut()

sunList = []

clock = pygame.time.Clock()

def main():
    running = True
    index = 0
    while running:
        if index >= 130:
            index = 0

        clock.tick(20)

        #2s产生一个太阳花
        if index % 40 == 0:
            sun = Sun(sunflower.rect)
            sunList.append(sun)



        screen.blit(bg_img_obj,(0,0))
        screen.blit(sunbank_img_obj,(250,0))
        screen.blit(sun_num_surface,(300,5))

        screen.blit(peashooter.images[index%13],peashooter.rect)
        screen.blit(sunflower.images[index % 13], sunflower.rect)
        screen.blit(wallnut.images[index % 13], wallnut.rect)

        for sun in sunList:
            screen.blit(sun.images[index % 17], sun.rect)


        index+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

if __name__ == '__main__':
    main()
