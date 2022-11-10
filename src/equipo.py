import jugador

class Equipo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []
    
    def añadir_jugador(self, jugador):
        self.jugadores.append(jugador)
