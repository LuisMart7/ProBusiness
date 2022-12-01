class Equipo:

    # El atributo jugadores debe ser una lista
    def __init__(self, nombre, jugadores):
        self.nombre = nombre
        self.jugadores = jugadores
        
    def añadir_jugador(self, jugador):
        self.jugadores.append(jugador)
