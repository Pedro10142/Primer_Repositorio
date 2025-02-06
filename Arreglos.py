
class Arreglo:
    def __init__(self):
        self.lista = []

    def mostrar(self):
        print(self.lista)
    
    def insertar(self):
        elemento = int(input("inserta el numero"))
        self.lista.append(elemento)
   
    def eliminar(self, elemento):
        self.elementos.remove(elemento)

    def modificar(self, i, elemento):
        self.elementos[i] = elemento

lista = Arreglo()
lista.mostrar()
lista.insertar