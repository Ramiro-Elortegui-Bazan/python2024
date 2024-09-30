class Personaje:
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.estado = True

    def atacar(self, otro_personaje):
        "Permite que un personaje ataque a otro."
        if not self.estado:
            print(f"{self.nombre} está muerto y no puede atacar.")
            return
        if not otro_personaje.estado:
            print(f"{otro_personaje.nombre} ya está muerto, no puede ser atacado.")
            return

        dano = max(self.fuerza - otro_personaje.resistencia, 1)
        print(f"{self.nombre} ataca a {otro_personaje.nombre} y causa {dano} de daño.")
        otro_personaje.recibir_dano(dano)

    def recibir_dano(self, cantidad):
        "Reduce la resistencia del personaje según la cantidad de daño recibido."
        self.resistencia -= cantidad
        if self.resistencia <= 0:
            self.resistencia = 0
            self.estado = False
            print(f"{self.nombre} ha muerto.")
        else:
            print(f"{self.nombre} ha recibido {cantidad} de daño. Resistencia restante: {self.resistencia}")
