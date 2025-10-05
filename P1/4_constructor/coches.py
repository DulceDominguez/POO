#Metodos getter y setter son importantes apra todas las clases para que el programador interactue cion los  valores de los atributos de los objetos atravez de estos metodos..dogamos que es la maneras mas adecuada para devolver o selccionar un valor (get), el set es para asignar un valor o para cambiar un atributo en particular
#atributo protegido<--- "_"
#El  metodo set siempre recibe parametros para cambiar el atributo del objeto
#Por cada uno de los atributos para pner un get
#Los metodos get siempre ingresan valor atravez de la propiedad return 
#FORMA1
class Coches:
    #Metodo contructor con este metodo se inicializan un objeto cuando es creado con valores iniciales 
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0
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
        pass
    def frenar():
        pass

#Objetos con valores;:
coche1=Coches()
coche1.set_marca("VM")
coche1.set_color("Blanco")
coche1.set_modelo(2022)
coche1.set_velocidad(220)
coche1.set_caballaje(150)
coche1.set_plazas(5)
coche1.no_seriie=12321
#print(f"Los valores del coche 1 son:{coche1.marca},{coche1.color},{coche1.modelo},{coche1.velocidad},{coche1.caballaje},{coche1.plazas}")
print(f"Los valores de coche 1 son:{coche1.get_valores()}")
#coche1=Coches("VM","Blanco","2022",220,150,5)---->Gtt de manera mas resumida

#COCHE 2
coche2=Coches()
coche2.set_marca("Nissan")
coche2.set_color("Azul")
coche2.set_modelo(202)
coche2.set_velocidad(100)
coche2.set_caballaje(150)
coche2.set_plazas(5)

#COCHE 3:
coche3=Coches()
coche3.set_marca("Honda")
print("Coche 3:Marca")

#print(f"Los valores del coche 2 son:{coche2.marca},{coche2.color},{coche2.modelo},{coche2.velocidad},
#{coche2.caballaje},{coche2.plazas}")
print(f"Los valores de coche 1 son:{coche1.get_valores()}")
#MULTIPLES OBJETOS:Crear objetos atravez de un mismo metodo
#Una de las ventajas de no tener un constructor es que podemos crear nuevos atributos del objeto
#################################################################################################

#FORMA 2
class Coches2:
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
        pass
    def frenar():
        pass

#Objetos con valores;:
coche1=Coches("VM","Blanco","2022",220,150,5,"12323")
#print(f"Los valores del coche 1 son:{coche1.marca},{coche1.color},{coche1.modelo},{coche1.velocidad},{coche1.caballaje},{coche1.plazas}")
print(f"Los valores de coche 1 son:{coche1.get_valores()}")
#coche1=Coches("VM","Blanco","2022",220,150,5)---->Gtt de manera mas resumida

#COCHE 2
coche2=Coches("Nissan","Azul","2020",180,150,6)

#COCHE 3:
coche3=Coches("Honda","","",0,0,0)#<-----No se pueden enviar mas de los parametros que estan declarados en el contructor, si solo se envia el valor de un atributo se debn enviar los otrso atributos vacios

#print(f"Los valores del coche 2 son:{coche2.marca},{coche2.color},{coche2.modelo},{coche2.velocidad},
#{coche2.caballaje},{coche2.plazas}")
print(f"Los valores de coche 1 son:{coche1.get_valores()}")
#MULTIPLES OBJETOS:Crear objetos atravez de un mismo metodo
#Una de las ventajas de no tener un constructor es que podemos crear nuevos atributos del objeto
#---La dirferencias de crear un constructor:no se tiene que hacer el set a menos que se quiera actualizar un valor 
#No es tan practico crear un atributo con valor vacio(forma1)
#Segunda froma mas dinamico y mayormente se utiliza mayormente