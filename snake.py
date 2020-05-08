import pygame
from pygame.locals import *

'''First Game'''

screen_size = (600, 600)

pygame.init()
screen = pygame.display.set_mode((screen_size))
pygame.display.set_caption('Game Snake')

snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill(255,255,255) #White

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
