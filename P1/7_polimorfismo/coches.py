
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

    
    @property
    def color(self):#<--Get
        return self._color
    @color.setter
    def color(self,color):
        self._color=color

     
    @property
    def modelo(self):#<--Get
        return self._modelo
    @modelo.setter
    def modelo(self,modelo):
        self._modelo=modelo

    @property
    def marca(self):#<--Get
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca=marca

    @property
    def velocidad(self):#<--Get
        return self._velocidad
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad=velocidad
    
    @property
    def caballaje(self):#<--Get
        return self._caballaje
    @caballaje.setter
    def caballaje(self,caballaje):
        self._caballaje=caballaje
    
    @property
    def plazas(self):#<--Get
        return self._plazas
    @plazas.setter
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
    @property
    def eje(self):
        return self.__eje
    @eje.setter
    def eje(self,eje):
        self.__eje=eje

    @property
    def capacidad_carga(self):
        return self.__capacidad_carga
    @capacidad_carga.setter
    def capacidad_carga(self,capacidad_carga):
        self.__capacidad_carga=capacidad_carga

    def acelerar():
        return "Estoy acelerando el camion"

    def frenar():
        return "Estoy frenando el camion"

    #METODOS
    def cargar(tipo_carga):
        __tipo_carga=tipo_carga
        return __tipo_carga
    

#CLASE CAMIONETA    

class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada

    @property
    def traccion(self):
        return self.__traccion
    @traccion.setter
    def traccion(self,traccion):
        self.__traccion=traccion

    @property
    def cerrada(self):
        return self.__cerrada
    @cerrada.setter
    def cerrada(self,cerrada):
        self.__cerrada=cerrada

    def acelerar():
        return "Estoy acelerando el camioneta"

    def frenar():
        return "Estoy frenando el camioneta"
    
    def transportar(num_pasajeros):
        __num_pasajeros=num_pasajeros
        return __num_pasajeros





