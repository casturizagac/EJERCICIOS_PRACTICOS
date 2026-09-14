class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print("Animal:", self.nombre)

class SerVivo:
    def __init__(self, vida):
        self.vida = vida

class Planta(SerVivo):
    def __init__(self, vida, tipo):
        super().__init__(vida)
        self.tipo = tipo

class Flor(Planta):
    def __init__(self, vida, tipo, color):
        super().__init__(vida, tipo)
        self.color = color

class AnimalClase(SerVivo):
    def __init__(self, vida, especie):
        super().__init__(vida)
        self.especie = especie

class Felino(AnimalClase):
    def __init__(self, vida, especie, garras):
        super().__init__(vida, especie)
        self.garras = garras

class Gato(Felino):
    def __init__(self, vida, especie, garras, raza):
        super().__init__(vida, especie, garras)
        self.raza = raza

class Leon(Felino):
    def __init__(self, vida, especie, garras, melena):
        super().__init__(vida, especie, garras)
        self.melena = melena

class Reptil(AnimalClase):
    def __init__(self, vida, especie, escamas):
        super().__init__(vida, especie)
        self.escamas = escamas

class Vivora(Reptil):
    def __init__(self, vida, especie, escamas, venenosa):
        super().__init__(vida, especie, escamas)
        self.venenosa = venenosa

class Rana(AnimalClase):
    def __init__(self, vida, especie, salto):
        super().__init__(vida, especie)
        self.salto = salto

class Roedor(AnimalClase):
    def __init__(self, vida, especie, dientes):
        super().__init__(vida, especie)
        self.dientes = dientes

class Raton(Roedor):
    def __init__(self, vida, especie, dientes, tamaño):
        super().__init__(vida, especie, dientes)
        self.tamaño = tamaño

class Conejo(Roedor):
    def __init__(self, vida, especie, dientes, orejas):
        super().__init__(vida, especie, dientes)
        self.orejas = orejas

class Humano(SerVivo):
    def __init__(self, vida, nombre):
        super().__init__(vida)
        self.nombre = nombre

class Niño(Humano):
    def __init__(self, vida, nombre, nivel):
        super().__init__(vida, nombre)
        self.nivel = nivel

class Adulto(Humano):
    def __init__(self, vida, nombre, trabajo):
        super().__init__(vida, nombre)
        self.trabajo = trabajo

class Anciano(Humano):
    def __init__(self, vida, nombre, edad):
        super().__init__(vida, nombre)
        self.edad = edad

gato = Gato(10, "Mamifero", "Si", "Persa")
niño = Niño(80, "Juan", "Primaria")
flor = Flor(1, "Planta", "Roja")

print(gato.raza)
print(niño.nivel)
print(flor.color)