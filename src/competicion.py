from dataclasses import dataclass

@dataclass
class Competicion:

    jornadas : list
    clasificacion : dict

    def __init__(self):
        self.jornadas = []
        self.clasificacion = []
