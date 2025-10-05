#Modelar y diagramar en la POO
print("Modelar y diagramar en la POO")
import os
print("cls")
class Coches:#<----clase de coches
    print("piiiii")
#Inicializar objetos 
coche1=Coches("Blanco","Toyota",220)
coche2=Coches("Amarillo","Nissan",180)
#Imprimir valores de objeto 1
print(f"Los valores del objeto 1 son:{coche1.marca}, {coche1.color}, {coche1.velocidad}")
print(f"El coche 1 acelero de:{coche1.velocidad} a {coche1.acelerar(50)}")
#Imprimir valores de objeto 2
print(f"Los valores del objeto 1 son:{coche2.marca}, {coche2.color}, {coche2.velocidad}")
print(f"El coche 1 acelero de:{coche2.velocidad} a {coche2.frenar(100)}")
#con el pass ponermos el metodo sin nada 
#Protegidos es cn un solo guion bajo, privado es con dos guin bajo 
#VERSION 2:
class Coches:#<----clase de coches
    def __init__(self,color,marca,velocidad):#<----metodo contructor que inicializa los valores de la clase coches
        #Atributos de coche 
        self.color=color
        self.marca=marca
        self.velocidad=velocidad
        #Si no tenemos el metodo constructor no se inicializa el objeto o no se instancia --udemi
        #Metodos o acciones del objeto 
        def acelerar(self,incremento):
            velocidad=incremento+1
            return self.velocidad
        def frenar(self,incremento):
            velocidad=incremento-1
            return self.velocidad
#Inicializar objetos 
coche1=Coches("Blanco","Toyota",220)
coche2=Coches("Amarillo","Nissan",180)
##############################################
#Version2:
#Modelar y diagramar en la POO
print("Modelar y diagramar en la POO")
import os
print("cls")
class Coches:#<----clase de coches
    print("piiiii")
#Inicializar objetos 
coche1=Coches("Blanco","Toyota",220)
coche2=Coches("Amarillo","Nissan",180)
#Imprimir valores de objeto 1
print(f"Los valores del objeto 1 son:{coche1.marca}, {coche1.color}, {coche1.velocidad}")
print(f"El coche 1 acelero de:{coche1.velocidad} a {coche1.acelerar(50)}")
#Imprimir valores de objeto 2
print(f"Los valores del objeto 1 son:{coche2.marca}, {coche2.color}, {coche2.velocidad}")
print(f"El coche 1 acelero de:{coche2.velocidad} a {coche2.frenar(100)}")
#con el pass ponermos el metodo sin nada 
#Protegidos es cn un solo guion bajo, privado es con dos guin bajo 
#VERSION 2:
#En publico y protegido si deja ver el valor del aributo del ovjeto, pero no es una buena practica , cuando sepas que vas a heredar
class Coches:#<----clase de coches
    print("piiii")
#Inicializar objetos 
coche1=Coches("Blanco","Toyota",220)
coche2=Coches("Amarillo","Nissan",180)











