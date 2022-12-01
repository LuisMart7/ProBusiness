from dataclasses import dataclass

@dataclass (frozen=True)
class Enfrentamiento:

    equipo1 :str
    equipo2 :str

    # Se entiende por equipo1 como el equipo local y equipo2 como equipo visitante
    def __init__(self, equipo1 :str, equipo2 :str):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
