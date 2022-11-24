class Enfrentamiento:

    # Se entiende por equipo1 como el equipo local y equipo2 como equipo visitante
    def __init__(self, equipo1, equipo2, goles1, goles2, fecha):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.goles1 = goles1
        self.goles2 = goles2
        self.fecha = fecha

    def get_enfrentamiento(self):
        return self.equipo1 + " - " + self.equipo2

    def get_resultado(self):
        return self.goles1 + " - " + self.goles2
