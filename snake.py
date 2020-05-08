import pygame
from pygame.locals import *
import random

'''First Game'''

screen_size = (600, 600)
white = (255, 255, 255)
red = (255, 0, 0)

#Position aleatory of target
def grid_random():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    
    return (x*10, y*10)

pygame.init()
screen = pygame.display.set_mode((screen_size))
pygame.display.set_caption('Game Snake')

#Snake
snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill(white)

#Target
target = pygame.Surface((10,10))
target.fill(red)
target_pos = grid_random()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
