import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from os.path import join

pygame.init()

# General setup
LARGHEZZA, ALTEZZA = 1024, 768
tmxdata = pytmx.TiledMap(".tiled\hub.tmx")
tiled_map = load_pygame('.tiled\hub.tmx')
screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Magic Adventure")
clock = pygame.time.Clock()

while True:
    
    deltaTime = clock.tick() / 1000
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    for layer in tiled_map.visible_layers:
        for x, y, gid, in layer:
            tile = tiled_map.get_tile_image_by_gid(gid)
            if(tile != None):
                screen.blit(tile, (x * tiled_map.tilewidth, y * tiled_map.tileheight))
        
    pygame.display.update()


pygame.quit()
