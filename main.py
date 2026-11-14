import pygame
from players import Player
from pygame.locals import *
import time
pygame.init()
pygame.font.init()

pygame.init()

font = pygame.font.SysFont("Arial", 40)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("bouncy game")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours 

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#load bg image
bg_image = pygame.image.load("assets/images/background/background.png").convert_alpha()

#load sprites
hhog1 = pygame.image.load("assets/images/sprites/hhog.png").convert_alpha()
hhog2 = pygame.image.load("assets/images/sprites/hhog2.png").convert_alpha()
tree1 = pygame.image.load("assets/images/foreground/tree1.png").convert_alpha()
flatmush = pygame.image.load("assets/images/foreground/flatmush.png").convert_alpha()
roundmush = pygame.image.load("assets/images/foreground/roundmush.png").convert_alpha()
groundtile = pygame.image.load("assets/images/foreground/groundtile.png").convert_alpha()
#background draw function
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#function for drawing health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, BLACK, (x - 5, y - 5, 410, 40))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

# Function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#ground height
GROUND_HEIGHT = 60

#function for drawing ground
def draw_ground():
    tile_width = groundtile.get_width()
    for i in range(0, SCREEN_WIDTH, tile_width):
        screen.blit(groundtile, (i, SCREEN_HEIGHT - GROUND_HEIGHT))

#player instances
player_1 = Player(200, 310, hhog1)
player_2 = Player(700, 310, hhog2)

#game loop
run = True
while run:

    clock.tick(FPS)

    #draw bg
    draw_bg()

    #draw ground
    draw_ground()

    #show player stats
    draw_health_bar(player_1.health, 20, 20)
    draw_health_bar(player_2.health, 580, 20)

    #move players
    if player_1.health > 0 and player_2.health > 0:
        player_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player_2, is_player_1 = True)
        player_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player_1, is_player_1 = False)

    #draw players
    player_1.draw(screen)
    player_2.draw(screen)

    #game over screen
    if player_1.health <= 0:
        draw_text("Player 2 Wins!", font, RED, SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 - 30)
    elif player_2.health <= 0:
        draw_text("Player 1 Wins!", font, RED, SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 - 30)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #update display
    pygame.display.update()
#exit pygame
pygame.quit()