import  pygame
from pygame.sprite import Sprite
from Configuracion import Configuracion

class Alien(Sprite):
    def __init__(self, juego):
        super().__init__()
        self.screen = juego.screen
        self.configuracion=juego.configuracion
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x=float(self.rect.x)

    """Mueve el alien"""
    def update (self):
        self.x+=(self.configuracion.alien_speed * self.configuracion.direccion)
        self.rect.x=self.x

    def bordes (self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True