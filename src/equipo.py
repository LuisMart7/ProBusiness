class Equipo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.estadisticas_jugadores = []
        self.partidos_jugados = 0
        self.victorias = 0
        self.empates = 0
        self.derrotas = 0
        self.puntos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        self.presupuesto_equipo = 0
        self.posicion_liga = 1
    
    def añadir_jugador(self, jugador):
        self.estadisticas_jugadores.append(jugador)

    def get_victorias(self):
        return self.victorias

    def get_derrotas(self):
        return self.derrotas

    def get_empates(self):
        return self.empates

    def get_goles_a_favor(self):
        return self.goles_a_favor

    def get_goles_en_contra(self):
        return self.goles_en_contra
