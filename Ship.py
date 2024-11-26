import pygame

class Nave:
    """Gestiona la nave del juego"""
    def __init__(self,juego):
        self.screen = juego.screen
        self.screen_rect = juego.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.configuracion=juego.configuracion
        self.x=float(self.rect.x)

    """Dibujar la nave del juego"""
    def colocar(self):
        self.screen.blit(self.image, self.rect)


    """Manejar movimiento"""
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.configuracion.velocidad_nave
        if self.moving_left and self.x > 0:
            self.x -= self.configuracion.velocidad_nave

        self.rect.x = self.x