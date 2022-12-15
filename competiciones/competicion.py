from dataclasses import dataclass
from typing import List
from jornada import Jornada

@dataclass
class Competicion:

    jornadas: List[Jornada]
    clasificacion: dict

    def __init__(self):
        self.jornadas = []
        self.clasificacion = {}
