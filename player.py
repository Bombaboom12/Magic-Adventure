from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("Images", "Mago", "Idle.png"))
        self.rect = self.image.get_frect(center = pos)

        # Movement 
        self.direction = pygame.Vector2()
        self.speed = 500

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            self.direction.y -= 1

        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, deltaTime):
        self.rect.x += self.direction.x * self.speed * deltaTime
        self.rect.y += self.direction.y * self.speed * deltaTime
        
    def collision(self, direction):
        pass

    def update(self, deltaTime):
        self.input()
        self.move(deltaTime)

