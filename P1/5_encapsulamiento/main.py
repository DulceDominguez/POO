#Instanciar los objetos para posteriormente implementarlos
from Coches import *
#import Coches

#Objetos con valores;:

#print(f"Los valores del coche 1 son:{coche1.marca},{coche1.color},{coche1.modelo},{coche1.velocidad},{coche1.caballaje},{coche1.plazas}")
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
    coche.acelerar()


