class Jugador:

    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.goles = 0
        self.asistencias = 0
        self.tarjetas_amarillas = 0
        self.tarjetas_rojas = 0
        self.minutos_jugados = 0
        self.valor_jugador = 0

    def incrementar_goles(self, nuevos_goles):
        self.goles += nuevos_goles

    def incrementar_asistencias(self, nuevas_asist):
        self.asistencias += nuevas_asist

    def incrementar_tarjetas_amarillas(self, nuevas_tarjetas_amarillas):
        self.tarjetas_amarillas += nuevas_tarjetas_amarillas

    def incrementar_tarjetas_rojas(self, nuevas_tarjetas_rojas):
        self.tarjetas_rojas += nuevas_tarjetas_rojas

    def incrementar_min_jugados(self, nuevos_min_jugados):
        self.minutos_jugados = nuevos_min_jugados

    def get_minutos_jugador(self):
        return self.minutos_jugados
