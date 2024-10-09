import pygame
from settings import *
from pytmx.util_pygame import load_pygame
from player import Player
from groups import *
from settore import *

pygame.init()

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
        pygame.display.set_caption("Magic Adventure")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = AllSprites()
        
        self.setup()

        self.player = Player((400, 680), self.all_sprites)
        
    def setup(self):
        map1 = load_pygame(join(".tiled", "Hub.tmx"))
        
        for layer in map1.visible_layers:
            for x, y, image in map1.get_layer_by_name(layer.name).tiles():
                Settore((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

    def run(self):
        while self.running:
            deltaTime = self.clock.tick() / 1000
    
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Draw the game
            self.all_sprites.update(deltaTime)
            # Draw
            self.screen.fill("Gray")
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()