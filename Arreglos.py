
class Arreglo:
    def __init__(self, elementos):
        self.elementos = elementos

    def mostrar(self):
        return self.elementos
    
    def insertar(self, elemento):
        self.elementos.append(elemento)
   
    def eliminar(self, elemento):
        self.elementos.remove(elemento)

    def modificar(self, i, elemento):
        self.elementos[i] = elemento

arreglo1 = Arreglo([1, 20, 30, 40])

while True:
    nuevo_elemento = input("Ingrese un nuevo elemento para insertar en la lista (o 'salir' para terminar): ")
    if nuevo_elemento.lower() == 'salir':
        break
    else:
        try:
            elemento = int(nuevo_elemento)
            arreglo1.insertar(elemento)
        except ValueError:
            print("Por favor, ingrese un número válido.")

print(arreglo1.mostrar())