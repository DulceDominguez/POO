
#FORMA 2
class Coches:
    #Metodo contructor con este metodo se inicializan un objeto cuando es creado con valores iniciales 
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas

    
    property
    def Color(self):#<--Get
        return self.color
    Color.setter
    def Color(self,color):
        self._color=color

     
    property
    def modelo(self):#<--Get
        return self.modelo
    modelo.setter
    def modelo(self,modelo):
        self._modelo=modelo

    property
    def marca(self):#<--Get
        return self.marca
    marca.setter
    def marca(self,marca):
        self._marca=marca

    property
    def velocidad(self):#<--Get
        return self.velocidad
    velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad=velocidad
    
    property
    def caballaje(self):#<--Get
        return self.caballaje
    caballaje.setter
    def caballaje(self,caballaje):
        self._caballaje=caballaje
    
    property
    def plazas(self):#<--Get
        return self.plazas
    plazas.setter
    def plazas(self,plazas):
        self._plazas=plazas


    def acelerar():
        return "Estoy acelerando el coche"

    def frenar():
        return "Estoy frenando el coche"

#CLASE CAMIONES:   
class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidad_carga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)#<--indicsa que se hereda, cuando sean dos se especifica de cual clase 
        self.__eje=eje
        self.__capacidad_carga=capacidad_carga

    #METODOS GEY Y SET
    property
    def eje(self):
        return self.eje
    eje.setter
    def eje(self,eje):
        self._color=eje

    property
    def capacidad_carga(self):
        return self.eje
    capacidad_carga.setter
    def capacidad_carga(self,capacidad_carga):
        self._color=capacidad_carga

    #METODOS
    def cargar(self,tipo_carga):
        self.__tipo_carga=tipo_carga
        return tipo_carga
    

#CLASE CAMIONETA    

class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada

    property
    def traccion(self):
        return self.__traccion
    traccion.setter
    def traccion(self,traccion):
        self.__traccion=traccion

    property
    def cerrada(self):
        return self.__cerrada
    cerrada.setter
    def cerrada(self,cerrada):
        self.__cerrada=cerrada
    
    def transportar(self,num_pasajeros):
        self.__num_pasajeros=num_pasajeros
        return self.__num_pasajeros


num=int(input("Cuantos coches deseas? "))
for i in range(0,num):
    print("Datos del coche: ")
    marca=input("\n\tIngresa la marca del coche: ").upper()
    color=input("\n\tIngresa el color del coche: ").upper()
    modelo=input("\n\tIngresa el modelo del coche: ").upper()
    velocidad=input("\n\tIngresa la velocidad del coche: ").upper()
    potencia=input("\n\tIngresa la potencia del coche: ").upper()
    plazas=input("\n\tIngresa las plazas del coche: ").upper()
    coche=Coches(marca,color,modelo,velocidad,potencia,plazas)
    print(f"Los valores de coche {num} son:{coche.get_valores()}")
    #coche.acelerar()


