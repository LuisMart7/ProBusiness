from dataclasses import dataclass
import enfrentamiento

@dataclass
class Jornada:

    enfrentamiento :list # Debe de ser un pair que incluya la clase enfrentamiento y el resultado (1, X o 2)

    def __init__(self):
        self.enfrentamiento = []
        
