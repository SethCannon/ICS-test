import pygame
import os, sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except (pygame.error, message):
        print ('Cannot load image:', name)
        raise (SystemExit, message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return (image, image.get_rect())

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

movespeed = 3
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        
                        
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue

                if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                        movespeed = movespeed*2

                if event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:
                        movespeed = movespeed/2
                        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= movespeed
        if pressed[pygame.K_DOWN]: y += movespeed
        if pressed[pygame.K_LEFT]: x -= movespeed
        if pressed[pygame.K_RIGHT]: x += movespeed
        screen.fill((255, 255, 255))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        #surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        load_image('face.png')

        

        clock.tick(60)
        
        pygame.display.flip()

