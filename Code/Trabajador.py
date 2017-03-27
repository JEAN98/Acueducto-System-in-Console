#Clase de los adiministradores y usuarios del sistema

class Trabajador:
    def __init__(self, cedula, nombre, edad, email, password, tipoTrabajador):

        self.cedula = cedula    #La cédula va ser el ID del trabajador
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.password = password
        self.tipoTrabajador = tipoTrabajador  # 1 = Admin , 2 = Users