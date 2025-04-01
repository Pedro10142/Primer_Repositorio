# CONJUNTOS
c = {1,2,3}

c.add(4) # añadir elemento
c.remove(1) # borrar si esta
c.discard(5) # borrar y si no esta sale del programa
print(c)
print(4 in c)

# EJERCICIO
# Crear un conjunto de 5 elementos
# Agregar un valor que no existe
# Eliminar un valor que no existe
# Verificar si existe un valor
# Agregar un valor repetido

print("EJERCICIO DE CONJUNTOS")
 
conjunto = {1.1, 1.2, 1.3, 1.4, 1.5}

conjunto.add(1.6)
conjunto.remove(1.2)
conjunto.discard(1.7)
print("¿Existe 1.8?", 1.8 in conjunto)
conjunto.add(1.1)

print(conjunto)
