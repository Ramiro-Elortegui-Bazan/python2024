import sqlite3

class Profesor:
    def __init__(self,nombre, materia, apellido):
        self.nombre = nombre
        self.materia = materia 
        self.apellido = apellido 
def guardar(self):
    conn = sqlite3.connect('escolar.db')
    c = conn.cursor()
    