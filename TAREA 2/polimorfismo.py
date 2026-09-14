class Auto:
    def __init__(self, marca, color="Blanco", gasolina=0):
        self.marca = marca
        self.color = color
        self.gasolina = gasolina

    def __iadd__(self, otro):
        self.gasolina += 5
        return self

    def __add__(self, otro):
        if isinstance(otro, str):
            self.color = otro
            return self

        if isinstance(otro, Auto):
            return self.gasolina + otro.gasolina

auto1 = Auto("Toyota")
auto2 = Auto("Nissan", "Rojo", 20)
print("Auto 1:", auto1.marca, auto1.color, auto1.gasolina)
print("Auto 2:", auto2.marca, auto2.color, auto2.gasolina)
auto1 += 5
print("Gasolina auto 1:", auto1.gasolina)
auto1 + "Azul"
print("Nuevo color:", auto1.color)
total = auto1 + auto2
print("Total de gasolina:", total)