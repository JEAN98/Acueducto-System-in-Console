"""Clase Padre"""
class Person:
    def __init__(self, cedula, nombre, edad, email):

        self.cedula = cedula  # La cédula va ser el ID de todas las personas
        self.nombre = nombre
        self.edad = edad
        self.email = email