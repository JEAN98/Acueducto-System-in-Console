"""Clase hija"""
from Person import *

class Subscriber(Person):
    def __init__(self, cedula, nombre, edad, email):
        Person.__init__(cedula,nombre,edad,email)