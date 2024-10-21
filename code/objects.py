from settings import *
from groups import *
from pygame import Color
from pytmx import load_pygame, TiledImageLayer, TiledTileLayer, TiledObjectGroup
from settore import *

class cambiozona(pygame.sprite.Sprite):

    def __init__(self, x, y, zona, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("Images", "Mago", "Idle.png"))
        self.rect = self.image.get_frect(center = (x,y))
        self.zona = zona
    
    def collision(self, game, cleanScreen):
        game.screen.blit(cleanScreen, ( 0, 0))
        pygame.display.update()
        all_sprites = AllSprites()
        zona = join(self.zona, ".tmx")
        zona = zona.replace("\\", "")
        map = load_pygame(join(".tiled", zona))
        for layer in map.visible_layers:
            if (isinstance( layer, TiledImageLayer)):
                image = map.get_tile_image_by_gid(layer.gid)
                if ( image ):
                    self.image = pygame.transform.scale(image,(LARGHEZZA, ALTEZZA))
            elif (isinstance( layer, TiledTileLayer)):
                for x, y, image in layer.tiles():
                    Settore((x * TILE_SIZE, y * TILE_SIZE), image, all_sprites)
            #elif (isinstance( layer, TiledObjectGroup)):
            #    for obj in layer:
            #        main.cambiozona = cambiozona(obj.x, obj.y, all_sprites)
        return all_sprites