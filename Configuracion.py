"""Configuraciones del juego"""
class Configuracion:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.velocidad_nave = 1.5
        self.bullet_spedd = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allow = 5
        self.alien_speed = 1.0
        self.drop_speed = 10
        self.direccion=1