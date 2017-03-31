"""Clase hija"""
from Person import *

class Worker(Person):
    def __init__(self, cedula, nombre, edad, email,passsword,tipoTrabajador):

        Person.__init__(self, cedula, nombre, edad, email)

        self.password = passsword
        self.tipoTrabajador = tipoTrabajador #1=Admin, 2=User