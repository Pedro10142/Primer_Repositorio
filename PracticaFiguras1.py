class Figura:
    def area(nl, l):
        if nl == 3:
            area = (l ** 2) * (3 ** 0.5) / 4
            return f"El area del triangulo es: {area}"
        elif nl == 4:
            area = l * l
            return f"El area del cuadrado es: {area}"
        elif nl == 5:
            area = (5 * l ** 2) / (4 * (5 - 2 * (5 ** 0.5)) ** 0.5)
            return f"El area del pentagono es: {area}"
        else:
            return "El calculo de area solo esta implementado para triangulos, cuadrados y pentagonos."
    def perimetro(nl, l):
        if nl in [3, 4, 5]:
            perimetro = nl * l
            return f"El perimetro es: {perimetro}"
        else:
            return "El calculo de perimetro solo esta implementado para triangulos, cuadrados y pentagonos."

nl = int(input("Ingresa el numero de lados (3 para triangulo, 4 para cuadrado, 5 para pentagono): "))
l = float(input("Ingresa la longitud de cada lado: "))

figura = Figura()
print(figura.area(nl, l))
print(figura.perimetro(nl, l))
    
        




        
    
        
        