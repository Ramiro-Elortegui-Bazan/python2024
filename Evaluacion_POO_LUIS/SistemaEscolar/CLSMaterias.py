import sqlite3

class Materia:
    def __init__(self,materia, curso,profesor):
        self.materia = materia
        self.curso = curso 
        self.profesor = profesor 
def guardar(self):
    conn = sqlite3.connect('escolar.db')
    c = conn.cursor()
    