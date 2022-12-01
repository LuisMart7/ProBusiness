from dataclasses import dataclass
import jornada

@dataclass
class Competicion:

    jornadas :list
    clasificacion :dict

    def __init__(self):
        self.jornadas = []
        self.clasificacion = []