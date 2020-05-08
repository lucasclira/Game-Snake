import pygame
from pygame.locals import *

'''First Game'''

screen_size = (600, 600)

pygame.init()
screen = pygame.display.set_mode((screen_size))
pygame.display.set_caption('Game Snake')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
