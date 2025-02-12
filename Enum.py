from enum import Enum
class Consecutivo(Enum):
    lunes = 1
    martes = 2
    miercoles = 3

print(Consecutivo.lunes)
print(Consecutivo.lunes.value)

print(type(Consecutivo.lunes))
print(type(Consecutivo.lunes.value))