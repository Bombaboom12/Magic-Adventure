import pygame
from os.path import join
from pytmx.util_pygame import load_pygame

pygame.init()

LARGHEZZA, ALTEZZA = 1280, 720
TILE_SIZE = 16

class Interface:

    def __init__(self):
        self.screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
        pygame.display.set_caption("Menu")
        self.font = pygame.font.Font(join("images", "font.otf"))
        self.bg = pygame.image.load(join("images", "background.jpg")).convert()
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):

        dt = self.clock.tick() / 1000
        self.screen.fill("aquamarine3")

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if start_button.collidepoint(mouse_pos):
                        game = Game()
                        game.run()
                    if exit_button.collidepoint(mouse_pos):
                        self.running = False
            
            text_start = self.font.render('Inizia', True, "white")
            text_instructions = self.font.render('Istruzioni', True, "white")
            text_exit = self.font.render('Esci', True, "white")

            start_button = pygame.Rect(150, 200, 200, 50)
            instructions_button = pygame.Rect(150, 270, 200, 50)
            exit_button = pygame.Rect(150, 340, 200, 50)

            pygame.draw.rect(self.screen, "black", start_button)
            pygame.draw.rect(self.screen, "black", instructions_button)
            pygame.draw.rect(self.screen, "black", exit_button)

            self.screen.blit(text_start, (160, 210))
            self.screen.blit(text_instructions, (160, 280))
            self.screen.blit(text_exit, (160, 350))

            pygame.display.update()

        pygame.quit()

class Game:

    class Player(pygame.sprite.Sprite):

        def __init__(self, pos, groups, collision_sprites):
            super().__init__(groups)
            self.image = pygame.image.load(join("Images", "Mago", "Idle.png"))
            self.rect = self.image.get_frect(center = pos)
            self.mask = pygame.mask.from_surface(self.image)
            self.collision_sprites = collision_sprites

            # Movement 
            self.direction = pygame.Vector2()
            self.speed = 500
            self.gravity = 5
            self.jumping = False
        
            def apply_gravity(self, deltaTime):
                self.direction.y += self.gravity * deltaTime
                self.rect.y += self.direction.y

            def collision(self, direction):
                for sprite in self.collision_sprites:
                    if sprite.mask.overlap(self.mask):
                        if direction == "horizontal":
                            pass
                        else:
                            pass
                
            def update(self, deltaTime):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.direction.x = 1
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0
                
                recent_keys = pygame.key.get_just_pressed()
                if recent_keys[pygame.K_SPACE]:
                    self.jumping = True

                self.direction = self.direction.normalize() if self.direction else self.direction

                self.rect.x += self.direction.x * self.speed * deltaTime
                self.apply_gravity(deltaTime)
                if self.jumping:
                    self.direction.y += -2
                    self.jumping = False

                self.rect.y += self.direction.y * self.speed * deltaTime

    class CollisionSprites(pygame.sprite.Sprite):
    
        def __init__(self, pos, surf, groups):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_frect(center = pos)

    class Settore(pygame.sprite.Sprite):
    
        def __init__(self, pos, surf, groups):
            super().__init__(groups)
            self.image = surf
            self.rect = self.image.get_frect(center = pos)

    class AllSprites(pygame.sprite.Group):

        def __init__(self):
            super().__init__()
            self.screen = pygame.display.get_surface()
            self.offset = pygame.Vector2()

        def draw(self, target_pos):
            self.offset.x = -(target_pos[0] - LARGHEZZA / 2)
            self.offset.y = -(target_pos[1] - ALTEZZA / 2)

            for sprite in self:
                self.screen.blit(sprite.image, sprite.rect.topleft + self.offset)

    def __init__(self):
        self.screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
        pygame.display.set_caption("Magic Adventure")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = self.AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        
        self.setup()
        
    def setup(self):
        map1 = load_pygame(join(".tiled", "Prova.tmx"))
        
        for x, y, image in map1.get_layer_by_name("Livello tile 1").tiles():
            self.Settore((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        for obj in map1.get_layer_by_name("Collisions"):
            self.CollisionSprites((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

        for obj in map1.get_layer_by_name("Characters"):
            if obj.name == "Player":
                self.player = self.Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)

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
    interface = Interface()
    interface.run()