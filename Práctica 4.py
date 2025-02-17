from enum import Enum
from typing import Final

class Usuario:
    max_Usuario: Final = 1000

    
class Dias(Enum):
    lunes = 1
    martes = 2
    miercoles = 3

horas_en_dia = {
    Dias.lunes: 12,
    Dias.martes: 10,
    Dias.miercoles: 19
}

print(Dias.lunes)
print(Dias.lunes.value)

print(type(Dias.lunes))
print(type(Dias.lunes.value))

for dia in Dias:
    print(f'{dia.name} tiene {horas_en_dia[dia]} horas')
