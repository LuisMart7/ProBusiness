from dataclasses import dataclass
from jornada import Jornada

@dataclass
class Competicion:

    jornadas : list(Jornada)
    clasificacion : dict

    def __init__(self):
        self.jornadas = []
        self.clasificacion = {}
