import sqlite3

class Calificacion:
    def __init__(self,id_estudiante, nota, fecha,id_materia):
        self.id_estudiante = id_estudiante
        self.nota = nota
        self.fecha = fecha
        self.id_materia = id_materia
def guardar(self):
    conn = sqlite3.connect('escolar.db')
    c = conn.cursor()