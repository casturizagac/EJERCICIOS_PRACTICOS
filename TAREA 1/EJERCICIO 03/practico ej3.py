class CuentaBancaria:
    def __init__(self, titular, nroCuenta, saldo):
        self.titular = titular
        self.nroCuenta = nroCuenta
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            print("Error: el monto a depositar debe ser mayor a 0.")
        else:
            self.saldo += monto
            print("Depósito realizado correctamente.")

    def retirar(self, monto):
        if monto > self.saldo:
            print("Error: no puede retirar más dinero del disponible.")
        elif monto <= 0:
            print("Error: el monto debe ser mayor a 0.")
        else:
            self.saldo -= monto
            print("Retiro realizado correctamente.")

    def mostrar_datos(self):
        print("\n--- DATOS DE LA CUENTA ---")
        print("Titular:", self.titular)
        print("Nro. de cuenta:", self.nroCuenta)
        print("Saldo:", self.saldo, "Bs")

cuenta = CuentaBancaria("Celina Asturizaga", "9144061", 1000)

cuenta.mostrar_datos()
cuenta.depositar(500)
cuenta.retirar(300)
cuenta.retirar(2000)
cuenta.depositar(-50)
cuenta.mostrar_datos()