import pygame
import os

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

def main():
    running = True

    while running:
        screen.blit(bg_img_obj,(0,0))
        screen.blit(sunbank_img_obj,(250,0))
        screen.blit(sun_num_surface,(300,5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

if __name__ == '__main__':
    main()
