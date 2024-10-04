import pygame
from settings import *
import pytmx
from pytmx.util_pygame import load_pygame
from player import Player
from os.path import join

pygame.init()



class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
        self.tmxdata = pytmx.TiledMap(".tiled\Hub.tmx")
        self.gameMap =  load_pygame(".tiled\Hub.tmx")
        pygame.display.set_caption("Magic Adventure")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            deltaTime = self.clock.tick() / 1000
    
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            for layer in self.gameMap.visible_layers:
                for x, y, gid, in layer:
                    tile = self.gameMap.get_tile_image_by_gid(gid)
                    if(tile != None):
                        self.screen.blit(tile, (x * self.gameMap.tilewidth, y * self.gameMap.tileheight))

            pygame.display.update()

        
pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()