import pygame
from os.path import join

pygame.init()

# General setup
LARGHEZZA, ALTEZZA = 1280, 720
screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Magic Adventure")
#icona = pygame.image.load(join())
#pygame.display.set_icon(icona)
clock = pygame.time.Clock()

running = True
while running:
    
    deltaTime = clock.tick() / 1000
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    screen.fill("Blue")

    pygame.display.update()

pygame.quit()
