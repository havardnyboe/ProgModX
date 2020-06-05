import pygame, sys, random as r, numpy as np

# initierer pygame
pygame.init()

# Oppsett av hovedvinduet
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('DVD')

# Klokke
clock = pygame.time.Clock()

# Farger
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = pygame.Color('black')

# Lager rektangler
dvdd = pygame.Rect(screen_width/2-8, screen_height/2-8, 16, 16)
dvd = pygame.image.load('dvd-logo.png')

speed_list = [] 
for i in np.arange(1.5,2.01,0.01):
    speed_list.append(round(i, 1))
    speed_list.append(round(i*-1, 1))

dvd_speed_x = r.choice(speed_list)
dvd_speed_y = r.choice(speed_list)

while True:
    # Event lytter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Game logic
    dvd.x += dvd_speed_x
    dvd.y += dvd_speed_y

    if dvd.left <= 0 or dvd.right >= screen_width:
        dvd_speed_x *= -1
    if dvd.top <= 0 or dvd.bottom >= screen_height:
        dvd_speed_y *= -1

    # Draw
    screen.fill(LIGHT_GRAY)
    screen.blit(dvd, (0,0))
    pygame.draw.rect(screen, DARK_GRAY, dvdd)

    # Oppdaterer vinduet
    pygame.display.flip()
    clock.tick(60)
