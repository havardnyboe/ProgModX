import pygame
import sys
import ball.py
import paddle.py

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

# Klokke
clock = pygame.time.Clock()

# Farger
white = (255, 255, 255)
black = (0, 0, 0)

# Lager objekter
ball = Ball()

while True:
    # Event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Game logic

    # Draw
    screen.fill(black)

    pygame.display.flip()

    clock.tick(60)
