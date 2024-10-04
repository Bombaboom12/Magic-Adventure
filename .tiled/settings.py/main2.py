from settings import *
from player import Player

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
        pygame.display.set_caption("Magic Adventure")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            deltaTime = self.clock.tick() / 1000
    
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Draw the game
            self.screen.fill("Blue")

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()