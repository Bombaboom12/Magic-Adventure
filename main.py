from settings import *
from player import Player
from groups import AllSprites
from settore import *
from pytmx.util_pygame import load_pygame

pygame.init()

class Game:

    def __init__(self):
        
        self.display_surf = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
        pygame.display.set_caption("Magic Adventure")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = AllSprites()
        self.player = Player((300, 700), self.all_sprites)
        self.setup()

    def setup(self):
        map1 = load_pygame(join(".tiled", "Hub.tmx"))
        map2 = load_pygame(join(".tiled", "Hub2.tmx"))
        
        for x, y, image in map1.get_layer_by_name("Livello tile 1").tiles():
            Settore((x * 16, y * 16), image, self.all_sprites)
        
    def run(self):
        while self.running:

            deltaTime = self.clock.tick() / 1000
    
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Draw the game
            self.all_sprites.update(deltaTime)
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()