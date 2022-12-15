from dataclasses import dataclass
from typing import List
from enfrentamiento import Enfrentamiento

@dataclass
class Jornada:

    # Debe de ser un pair que incluya la clase enfrentamiento y el resultado (1, X o 2)
    enfrentamientos: List[Enfrentamiento]

    def __init__(self):
        self.enfrentamientos = []
