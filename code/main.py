import pygame
from objects import cambiozona
from settings import *
from pytmx import load_pygame, TiledImageLayer, TiledTileLayer, TiledObjectGroup
from player import Player
from groups import *
from settore import *


pygame.init()

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
        self.cleanScreen = self.screen.copy()
        pygame.display.set_caption("Magic Adventure")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = AllSprites()
        
        self.setup()

        self.player = Player((400, 680), self.all_sprites)
        
    def setup(self):
        map = load_pygame(join(".tiled", "Hub.tmx"))
        #TiledImage disegnata a schermo        
        for layer in map.visible_layers:
            if (isinstance( layer, TiledImageLayer)):
                image = map.get_tile_image_by_gid(layer.gid)
                if ( image ):
                    self.image = pygame.transform.scale(image,(LARGHEZZA, ALTEZZA))
            elif (isinstance( layer, TiledTileLayer)):
                for x, y, image in layer.tiles():
                    Settore((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
            elif (isinstance( layer, TiledObjectGroup)):
                for obj in layer:
                    self.cambiozona = cambiozona(obj.x, obj.y, obj.properties['zona'] ,self.all_sprites)
                    
                    
                

    def run(self):
        while self.running:
            self.deltaTime = self.clock.tick() / 1000
    
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                point = self.player.rect.center
                collide = self.cambiozona.rect.collidepoint(point)
                if collide:
                    self.all_sprites = self.cambiozona.collision(self, self.cleanScreen)
                    self.player = Player((200, 680), self.all_sprites) 

            # Draw the game
            self.all_sprites.update(self.deltaTime)
            # Draw
            self.screen.fill("Gray")
            self.screen.blit( self.image, ( 0, 0))
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()