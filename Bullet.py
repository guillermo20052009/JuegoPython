import pygame
from pygame.sprite import Sprite
"""Clase que manejará el comportamiento de las balas"""
class Bullet(Sprite):
    def __init__(self, juego):
        super().__init__()
        self.screen = juego.screen
        self.configuracion=juego.configuracion
        self.color=self.configuracion.bullet_color

        self.rect=pygame.Rect(0,0,self.configuracion.bullet_width,self.configuracion.bullet_height)
        self.rect.midtop=juego.nave.rect.midtop

        self.y=juego.nave.rect.y
