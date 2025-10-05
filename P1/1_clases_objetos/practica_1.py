#Calcular el area del resctangulo con programacion estructurada y poo
#Programacion estructurada
def Calcular():
    base=input("Ingrese la base del rectangulo: ")
    altura=input("Ingrese la altura del rectangulo: ")
    multiplicacion=base*altura
    return multiplicacion
print(F"El area del rectangulo es:{Calcular()}")
print()
#POO
class AreaRectangulo:
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def areaRectangulo(b,h):
        area=b*h
        return area
rectangulo=AreaRectangulo(7,8)
print(F"El area del rectangulo es:{rectangulo.areaRectangulo()}")
