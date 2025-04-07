dic = {"x":"equis", "y":"ye", "d":"de"}
dic2 = dict(x="equis", y="ye", d="de") # convertir lista a diccionario

# print(dic["z"]) # error al buscar elemento que no existe
print(dic.get("z")) # si el elemento no existe retorna nulo
dic["x"] = "equisD" # modificar valor del elemento
dic["z"] = "zeta"

print("x" in dic)
print(dic2)
print(dic)
llaves = dic.keys() # llaves de todo el diccionario
valores = dic.values() # valores de todo el diccionario
p = dic.items() # convertir a tuplas el diccionario

print(llaves)
print(valores)
print(p)