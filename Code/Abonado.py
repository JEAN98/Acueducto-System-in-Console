#Clase para los abonados del sistema

class Abonado:
    def __init__(self, cedula, nombre, direccion, telefono):

        self.cedula = cedula    #La cédula va ser el ID del abonado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
