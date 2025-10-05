
class Calculadora:
    def __init__(self):
        self.__num1=int(input("Ingrese un numero entero: "))
        self.__num2=int(input("Ingrese otro numero entero: "))

    @property
    def num1(self):
        return self.__num1
    @num1.setter
    def num1(self,num1):
        self.__num1=num1

    @property
    def num2(self):
        return self.__num2
    @num2.setter
    def num2(self,num2):
        self.__num2=num2
    
    def sumar(self):
        suma=self.__num1+self.__num2
        return suma
    
    def restar(self):
        resta=self.__num1-self.__num2
        return resta

    def multiplicar(self):
        multiplicacion=self.__num1*self.__num2
        return multiplicacion
    
    def dividir(self):
        division=self.__num1/self.__num2
        return division

operacion=Calculadora()
print(operacion.sumar())
print(operacion.multiplicar())
print(operacion.dividir())
print(operacion.restar())

        
        
    