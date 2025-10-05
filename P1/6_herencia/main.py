#Instanciar los objetos para posteriormente implementarlos
from Coches import Camionetas,Camiones,Coches
#import Coches

#Objetos con valores:

#print(f"Los valores del coche 1 son:{coche1.marca},{coche1.color},{coche1.modelo},{coche1.velocidad},{coche1.caballaje},{coche1.plazas}")
#Un atributo privado no se puede heredar,mayormente se dejan protegidos para que puedan heredarse aotras clases
coche=Coches("Nissan","Azul","2020",180,150,6)
coche.acelerar()
camioneta=Camionetas()
camion=Camiones()

