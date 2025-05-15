# CONJUNTOS

print("EJEMPLO DE CONJUNTO")

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
conjunto2 = {1,2,3,8,9}

conjunto.add(1.6)
conjunto.remove(1.2)
conjunto.discard(1.7)
print("¿Existe 1.8?", 1.8 in conjunto)
conjunto.add(1.1)
print(conjunto)

print("CONEXIONES LOGICAS")
C = {1,2,3}
C2 = {3,4,5}

u = C.union(C2) # or u = C | C2
i = C.intersection(C2) # or i = C & C2
d = C.difference(C2) # or d = C - C2
ds = C.symmetric_difference(C2) # C ^ C2

print(u)
print(i)
print(d)
print(ds)

print("OTRAS FUNCIONES")

a = {1,2,3}
b = {1,2,3,4,5}
c = {}
d = set()

a.issubset(b)
d.issubset(b)
b.issuperset(a)
print(type(c))




