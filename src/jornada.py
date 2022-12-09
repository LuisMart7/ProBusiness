from dataclasses import dataclass

@dataclass
class Jornada:

    # Debe de ser un pair que incluya la clase enfrentamiento y el resultado (1, X o 2)
    enfrentamiento : list

    def __init__(self):
        self.enfrentamiento = []
