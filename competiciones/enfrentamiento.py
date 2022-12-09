from dataclasses import dataclass

@dataclass (frozen=True)
class Enfrentamiento:

    equipo1 : str
    equipo2 : str
    goles1 : int
    goles2 : int

    # Se entiende por equipo1 como el equipo local y equipo2 como equipo visitante
    def __init__(self, equipo1 :str, equipo2 :str, goles1 :int, goles2 :int):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.goles1 = goles1
        self.goles2 = goles2
