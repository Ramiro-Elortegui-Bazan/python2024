class Personaje:
    estado = True  # indica si esta vivo o muerto 
    vida = 100
    def __init__(self, nombre,resistencia, ataque):
        self.nombre = nombre
        self.resistencia = resistencia
        self.ataque = ataque
        
