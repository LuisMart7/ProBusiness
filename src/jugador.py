class Jugador:

    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        
    def get_nombre(self):
        return self.nombre
    
    def get_posicion(self):
        return self.posicion