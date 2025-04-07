import math

class Figura:
    def poli(lado, nLados):
        if nLados>4:
            A = (nLados * (lado * lado)) / (4 * math.tan(math.pi / nLados))
            P = lado * nLados
            return P, A
        else:
            P=None
            A=None
            return P, A

lado = float(input("Ingresa la longitud de un lado: "))
nLados = int(input("Ingresa el número de lados del polígono: "))
perimetro, area = Figura.poli(lado, nLados)
print("El perímetro es:", perimetro)
print("El área es:", area)