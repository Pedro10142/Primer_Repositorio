from abc import ABC, abstractmethod

class Padres(ABC):
    @abstractmethod
    def rasgos(self):
        pass

class hijo1(Padres):
    def rasgos(self):
        return "color de piel"

class hijo2(Padres):
    def rasgos(self):
        return "color de ojos"

hijo1 = hijo1()
hijo2 = hijo2()

print("hijo1 ", hijo1.rasgos())
print("hijo2 ", hijo2.rasgos())
