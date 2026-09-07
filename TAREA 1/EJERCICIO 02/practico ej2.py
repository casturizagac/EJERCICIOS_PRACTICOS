class Computadora:
    def __init__(self, marca, procesador, ram, almacenamiento):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento

    def mostrar_datos(self):
        print("Marca:", self.marca)
        print("Procesador:", self.procesador)
        print("RAM:", self.ram, "GB")
        print("Almacenamiento:", self.almacenamiento, "GB")

computadora1 = Computadora("Lenovo", "Intel Core i5", 8, 512)

computadora2 = Computadora(
    marca="HP",
    procesador="AMD Ryzen 5",
    ram=16,
    almacenamiento=1000
)

print("COMPUTADORA 1")
computadora1.mostrar_datos()

print("\nCOMPUTADORA 2")
computadora2.mostrar_datos()

X = int(input("\nIngrese la cantidad de RAM X: "))

if computadora1.ram == X:
    print("La computadora 1 tiene RAM igual a X.")
else:
    print("La computadora 1 NO tiene RAM igual a X.")

if computadora2.ram == X:
    print("La computadora 2 tiene RAM igual a X.")
else:
    print("La computadora 2 NO tiene RAM igual a X.")

print("\nCOMPUTADORA CON MAYOR ALMACENAMIENTO")

if computadora1.almacenamiento > computadora2.almacenamiento:
    computadora1.mostrar_datos()
elif computadora2.almacenamiento > computadora1.almacenamiento:
    computadora2.mostrar_datos()
else:
    print("Las dos computadoras tienen el mismo almacenamiento.")