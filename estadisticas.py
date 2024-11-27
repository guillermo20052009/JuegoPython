

class Estadisticas:
    def __init__(self,juego):
        self.configuracion = juego.configuracion
        self.reiniciar()
        self.activo = True

    def reiniciar(self):
        self.ships_left = self.configuracion.vidas