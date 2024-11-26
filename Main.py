import sys
import pygame
from Configuracion import Configuracion
from Ship import Nave
from Bullet import Bullet

"""Clase que controla el funcionamiento del juego"""
class AlienInvasion:
    def __init__(self):
        """Inicializa Juego"""
        pygame.init()

        self.configuracion = Configuracion()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.configuracion.screen_width = self.screen.get_rect().width
        self.configuracion.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.nave = Nave(self)
        self.bullets=pygame.sprite.Group()

    """Inicia el juego principal"""
    def run_game(self):
        while True:
            self.check_events()
            self.nave.update()
            self.bullets.update()
            self.borrar_balas()
            self.update_screen()

    """Escucha eventos del teclado"""
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.mov_derecha(event)
            self.mov_izquierda(event)
            self.terminar_juego(event)
            self.disparar(event)


    """Actualiza la pantalla"""
    def update_screen(self):
        self.screen.fill(self.configuracion.bg_color)
        self.nave.colocar()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()



    """Maneja el movimiento a la derecha"""
    def mov_derecha(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.nave.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                 self.nave.moving_right = False


    """Maneja el movimiento a la izquierda"""
    def mov_izquierda(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.nave.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.nave.moving_left = False

    """Terminar Juego"""
    def terminar_juego(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

    """Se encarga de registrar las pulsaciones de espacio"""
    def disparar (self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.fire_bullet()

    """Dibuja la bala"""
    def fire_bullet(self):
        if len(self.bullets) < self.configuracion.bullet_allow:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    """Borra las balas que llegan arriba del todo"""
    def borrar_balas(self):
        for bullet in self.bullets.copy():
            if bullet.rect.y <=0:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    juego = AlienInvasion()
    juego.run_game()