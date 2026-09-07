class Auto:
    def __init__(self, marca, modelo, anio, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.color = "Sin color"

    def mostrar_kilometraje(self):
        metros = self.kilometraje * 1000
        print("Kilometraje:", self.kilometraje, "km")
        print("Kilometraje:", metros, "m")

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print("El nuevo color es:", self.color)

auto1 = Auto("Toyota", "Rush", 2020, 15000)
auto2 = Auto("Ford", "Mustang", 2000, 23000)

auto1.cambiar_color("Rojo")
auto2.cambiar_color("Plomo")

print("Auto 1:")
auto1.mostrar_kilometraje()

print("Auto 2:")
auto2.mostrar_kilometraje()