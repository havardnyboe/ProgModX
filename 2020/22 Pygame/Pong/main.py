import pygame
import sys
import random as r
import numpy as np

# initierer pygame
pygame.init()

# Oppsett av hovedvinduet
screen_width = 1100
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Klokke
clock = pygame.time.Clock()

# Farger
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = pygame.Color("grey12")


def ball_move():
    ball.x += ball_speed_x
    ball.y += ball_speed_y


def player_move():
    player.y += player_speed_y


def opponent_ai():
    global opponent_speed_y
    if ball.top < opponent.top + 60 and ball.x > screen_width - screen_width / 2.5:
        opponent_speed_y = -5
    elif ball.bottom > opponent.bottom - 60 and ball.x > screen_width - screen_width / 2.5:
        opponent_speed_y = 5
    opponent.y += opponent_speed_y


def player_ai():
    # global player_speed_y
    if ball.top > player.top - 60:
        player_speed_y = -5
    if ball.bottom > player.bottom - 60:
        player_speed_y = 5
    player.y += player_speed_y


def check_collition():
    global ball_speed_x, ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        game_over()
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def game_over():
    pygame.quit()
    sys.exit()


# Lager rektangler #
ball = pygame.Rect(screen_width / 2 - 8, screen_height / 2 - 8, 16, 16)
player = pygame.Rect(10, screen_height / 2 - 70, 7, 120)
opponent = pygame.Rect(screen_width - 17, screen_height / 2 - 70, 7, 120)

ball_speed_x = r.choice((5, -5))
ball_speed_y = r.choice((5.2, -5.2))
player_speed_y = 0
opponent_speed_y = 0

# Game Loop #
while True:
    # Event lytter #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed_y = -5
            if event.key == pygame.K_DOWN:
                player_speed_y = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed_y = 0
            if event.key == pygame.K_DOWN:
                player_speed_y = 0

    # Game logic #
    ball_move()
    player_move()
    # player_ai()
    opponent_ai()
    check_collition()

    # Draw #
    screen.fill(DARK_GRAY)

    pygame.draw.ellipse(screen, LIGHT_GRAY, ball)
    pygame.draw.rect(screen, LIGHT_GRAY, player)
    pygame.draw.rect(screen, LIGHT_GRAY, opponent)

    # Oppdaterer vinduet #
    pygame.display.flip()
    clock.tick(60)
