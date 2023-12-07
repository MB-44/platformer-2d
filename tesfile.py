import os
import math
import random
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("2d platformer game")

bgColor = (255,255,255)
WIDTH, HEIGHT = (800,600)
FPS = 50
playerVelocity = 5

window = pygame.display.set_mode((WIDTH,HEIGHT))

def getBackground(name):
    image = pygame.image.load(join("assets","Background",name))
    _, _, width, height = image.get_rect() # _, _, ---> x,y --> _ because I dont care about x, y value
    tiles = []

    for i in range(WIDTH//width+1):
        for j in range(HEIGHT//height+1):
            position = [i * width, j * height]
            tiles.append(position)
    return tiles,image

    
def draw(window, background, bgImage):
    for tile in background:
        window.blit(bgImage, tuple(tile))
    
    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    background,bgImage = getBackground("Blue.png")

    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, background,bgImage)
        
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)