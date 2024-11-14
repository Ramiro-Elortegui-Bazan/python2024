import sqlite3

class Estudiante:
    def __init__(self,legajo_id,nombre, edad, curso,fecha_nacimiento,dni):
        self.legajo_id   = legajo_id
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni
    
    def guardar(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()   