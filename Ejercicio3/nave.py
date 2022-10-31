class Nave():

    def __init__(self,nombre, largo, tripulacion, npasajeros):
        self.nombre=nombre
        self.largo=largo
        self.tripulacion=tripulacion
        self.npasajeros=npasajeros

    def __str__(self):
        return "La nave {}, tiene {} metros de largo, {} tripulantes y {} pasajeros".format( self.nombre, self.largo, self.tripulacion, self.npasajeros)

    def get_nombre(self):
        return self.nombre
    def get_largo(self):
        return self.largo
    def get_tripulacion(self):
        return self.tripulacion
    def get_npasajeros(self):
        return self.npasajeros
