import pygame, sys, random as r, numpy as np

# initierer pygame
pygame.init()

# Oppsett av hovedvinduet
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Klokke
clock = pygame.time.Clock()

# Farger
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = pygame.Color('grey12')

# Lager rektangler
ball = pygame.Rect(screen_width/2-8, screen_height/2-8, 16, 16)
player = pygame.Rect(10, screen_height/2 - 70, 7, 120)
opponent = pygame.Rect(screen_width - 20, screen_height/2 - 70, 7, 120)

speed_list = [] 
for i in np.arange(3,3.51,0.01):
    speed_list.append(round(i, 1))
    speed_list.append(round(i*-1, 1))

ball_speed_x = r.choice(speed_list)
ball_speed_y = r.choice(speed_list)

while True:
    # Event lytter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Game logic
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Draw
    screen.fill(DARK_GRAY)

    pygame.draw.ellipse(screen, LIGHT_GRAY, ball)
    pygame.draw.rect(screen, LIGHT_GRAY, player)
    pygame.draw.rect(screen, LIGHT_GRAY, opponent)

    # Oppdaterer vinduet
    pygame.display.flip()
    clock.tick(60)
