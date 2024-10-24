import sqlite3

class Materia:
    def __init__(self,nombre, edad, año_id):
        self.nombre = nombre
        self.edad = edad
        self.año_id = año_id
def guardar(self):
    conn = sqlite3.connect('escolar.db')
    c = conn.cursor()
    