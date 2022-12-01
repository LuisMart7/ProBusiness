from dataclasses import dataclass
import enfrentamiento

@dataclass
class Jornada:

    enfrentamiento :list
    resultados :list
    goles :list

    def __init__(self):
        self.enfrentamiento = []
        self.resultados = []
        self.goles = []
