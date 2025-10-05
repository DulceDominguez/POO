
#FORMA 2
class Coches:
    #Metodo contructor con este metodo se inicializan un objeto cuando es creado con valores iniciales 
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas
    def set_marca(self,marca):
        self.__marca=marca
    def set_color(self,color):
        self.__color=color
    def set_modelo(self,modelo):
        self.__modelo=modelo
    def set_velocidad(self,velocidad):
        self.__velocidad=velocidad
    def set_caballaje(self,caballaje):
        self.__caballaje=caballaje
    def set_plazas(self,plazas):
        self.__plazas=plazas
    def get_valores(self):
        return self.__marca,self.__color,self.__modelo,self.__velocidad,self.__caballaje,self.__plazas
    def acelerar():
        return print("Estoy acelerando el coche")

    def frenar():
        return print("Estoy frenando el coche")

