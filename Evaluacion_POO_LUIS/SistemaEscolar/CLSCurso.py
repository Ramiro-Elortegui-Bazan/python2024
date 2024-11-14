import sqlite3
class curso:
    def __init__(self,id_curso, nombre):
        self.id_curso  = id_curso
        self.nombre = nombre
    
    
def guardar(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()   