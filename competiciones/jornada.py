from dataclasses import dataclass
from enfrentamiento import Enfrentamiento

@dataclass
class Jornada:

    # Debe de ser un pair que incluya la clase enfrentamiento y el resultado (1, X o 2)
    enfrentamientos : list(Enfrentamiento)

    def __init__(self):
        self.enfrentamientos = []
