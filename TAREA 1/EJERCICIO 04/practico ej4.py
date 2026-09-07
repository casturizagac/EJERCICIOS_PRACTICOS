class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.dinero = 0

    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
            print(cantidad, "pasajeros subieron al bus.")
        else:
            disponibles = self.capacidad - self.pasajeros
            print("No pueden subir todos.")
            print("Solo hay", disponibles, "asientos disponibles.")

    def cobrar_pasaje(self):
        costo = 1.50

        if self.pasajeros > 0:
            total = self.pasajeros * costo
            self.dinero += total
            print("Se cobraron Bs.", total)
        else:
            print("No hay pasajeros para cobrar.")

    def mostrar_asientos_disponibles(self):
        disponibles = self.capacidad - self.pasajeros
        print("Asientos disponibles:", disponibles)

bus = Bus(30)

bus.subir_pasajeros(10)
bus.cobrar_pasaje()
bus.mostrar_asientos_disponibles()
bus.subir_pasajeros(5)
bus.cobrar_pasaje()
bus.mostrar_asientos_disponibles()