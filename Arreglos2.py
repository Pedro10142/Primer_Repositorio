class Arreglo:
    def __init__(self, elementos):
        self.elementos = elementos

    def mostrar(self):
        return self.elementos
    
    def insertar(self):
        elemento = int(input("Ingrese el elemento que desea insertar: "))
        self.elementos.append(elemento)

arreglo1 = Arreglo([1, 2, 4, 5])

arreglo1.insertar()

print(arreglo1.mostrar())
