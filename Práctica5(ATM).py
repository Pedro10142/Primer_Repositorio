class ATM:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        print(f"Su saldo actual es: ${self.saldo:.2f}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Ha depositado ${cantidad:.2f}. Su nuevo saldo es: ${self.saldo:.2f}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Ha retirado ${cantidad:.2f}. Su nuevo saldo es: ${self.saldo:.2f}")
        elif cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def ejecutar(self):
        while True:
            print("\n--- Bienvenido al Cajero Automático ---")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.consultar_saldo()
            elif opcion == "2":
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                self.depositar(cantidad)
            elif opcion == "3":
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                self.retirar(cantidad)
            elif opcion == "4":
                print("Gracias por usar el cajero automático. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

# Crear una instancia de la clase ATM e iniciar el sistema
atm = ATM(1000)  # Saldo inicial de $1000
atm.ejecutar()
