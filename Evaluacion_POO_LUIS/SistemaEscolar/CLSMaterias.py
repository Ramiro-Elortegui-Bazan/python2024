import sqlite3

class Materia:
    def __init__(self,id_materia,nombre,curso,):
        self.id_materia = id_materia
        self.nombre = nombre
        self.curso = curso 
def guardar(self):
    conn = sqlite3.connect('escolar.db')
    c = conn.cursor()
    