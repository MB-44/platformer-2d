import os, random, math, pygame
from os import listdir
from os.path import join, isfile

pygame.init()

bgColor = (255,255,255)
WIDTH, HEIGHT = (800,600)
FPS = 50
playerVelo = 5

pygame.display.set_caption("2D platformer game")
window = pygame.display.set_mode((WIDTH,HEIGHT))


class Player(pygame.sprite.Sprite):
    COLOR = (255,0,0)
    GRAVITY = 1

    # initialising variables
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.xVelo = 0
        self.yVelo = 0
        self.mask = None
        self.direction = "left"
        self.animationCount = 0
        self.fallCount = 0

    # getting the positions for some movement
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    # if the player wants to move left it will substract, 
    def moveLeft(self, velo):
        self.xVelo = -velo
        if self.direction != "left":
            self.direction = "left"
            self.animationCount = 0

    def moveRight(self, velo):
        self.xVelo = velo
        if self.direction != "right":
            self.direction = "right"
            self.animationCount = 0
    
    def loop(self, fps):
        self.yVelo += min(1, (self.fallCount / fps) * self.GRAVITY)
        self.move(self.xVelo, self.yVelo)

        self.fallCount += 1

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)


# importing the background image & store the position of the background tiles
def getBackground(name):
    image = pygame.image.load(join("assets","Background",name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            position = [i * width, j * height]
            tiles.append(position)
    return tiles, image


# this will draw the background image one by one and after all of that
# display will update
def draw(window, background, bgImage, player):
    for tile in background:
        window.blit(bgImage, tuple(tile))
    
    player.draw(window)
    
    pygame.display.update()


def handleMove(player):
    keys = pygame.key.get_pressed()

    player.xVelo = 0
    if keys[pygame.K_LEFT]:
        player.moveLeft(playerVelo)
    if keys[pygame.K_RIGHT]:
        player.moveRight(playerVelo)






# just a main function - it's all happening here
def main(window):
    clock = pygame.time.Clock()
    background, bgImage = getBackground("Blue.png")

    player = Player(100,100, 50,50)

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        player.loop(FPS)
        handleMove(player)
        draw(window, background, bgImage, player)
    
    pygame.quit()
    quit()



if __name__ == "__main__":
    main(window)
        