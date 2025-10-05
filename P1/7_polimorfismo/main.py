from Coches import *
import os
def main():
    #Instanciar los objetos para posteriormente implementarlos
    #Si tengo muchas clases en un modulo se debe poner solo las clases que se utilizaran
    #import Coches<---debo usar from coches import * para poder utilizar todas las clases y metodos que tenga dentro del archivo o modulo llamado coches
    #from Coches import Camionetas,Camiones,Coches<----No es una buena practica
    def BorrarPantalla():
        print("cls")

    def EspereTecla():
        input("\n\tOprima una tecla para continuar...")

    def Datos_Vehiculos(Tipo):
        BorrarPantalla()
        print(f"Ingresar los datos del vehiculo de tipo {Tipo}: ")
        marca=input("\n\tMarca: ").upper()
        color=input("\n\tColor: ").upper()
        modelo=input("\n\tModelo: ").upper()
        velocidad=input("\n\tVelocidad: ").upper()
        potencia=input("\n\tPotencia: ").upper()
        plazas=input("\n\tN° de plazas: ").upper()
        return marca,color,modelo,velocidad,potencia,plazas

    def Imprimir_Datos(marca,color,modelo,velocidad,potencia,plazas):
        print(f"Datos del coche:\n  Marca:{marca} \n Color:{color} \n Modelo:{modelo} \n Velocidad:{velocidad} \n Potencia:{potencia} \n Plazas:{plazas}" )

    def Auto():
        marca,color,modelo,velocidad,potencia,plazas=Datos_Vehiculos("Auto")
        coche=Coches(marca,color,modelo,velocidad,potencia,plazas)
        Imprimir_Datos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)

    def Camion():
        marca,color,modelo,velocidad,potencia,plazas=Datos_Vehiculos("Camion")
        eje=input("\n\tN° eje: ").upper()
        capacidad_carga=input("\n\tCapacidad de carga: ").upper()
        coche=Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidad_carga)
        Imprimir_Datos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        print(f"\neje:{coche.eje}\n capacidad:{coche.capacidad_carga}" )

    def Camioneta():
        marca,color,modelo,velocidad,potencia,plazas=Datos_Vehiculos("Camioneta")
        traccion=input("\n\tTraccion: ").upper()
        es_cerrada=input("\n\tEs cerrada? si/no: ").upper()
        if es_cerrada=="SI":
            cerrada=True
        elif es_cerrada=="NO":
            cerrada=False
        coche=Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
        Imprimir_Datos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        print(f"\n Traccion:{coche.traccion}\n cerrada:{coche.cerrada}" )

    #todo el codigo es el controlador
    opcion=True
    while opcion:
        print("\n\t.::Menu principal::.\n1.-Coche\n2.-Camioneta\n3.-Camion\n4.-Salir")
        opcion=input("Elije una opcion: ")#opciones de la vista(input,print) todo lo demas es el controlador, la clase es el modelo
        match(opcion):
            case "1":
                Auto()
            case "2":
                Camioneta()
            case "3":
                Camion()
            case "4":
                print("\n\tGracias por usar el sitema!!")
                EspereTecla()
                opcion=False
            case _:
                print("Opcion no valida, por favor vuelva a intentarlo...")

        #El break no significa lo mismo que el break en switch, en switch es crucial mientras que aqui rompe todo el codigo de todo el programa y se usa con discrecion 
        #Si se repite el codigo es mejor ponerlo en una funcion


if __name__=="__main__":
    main()

#MMODELO VISTA CONTROLADOR:patron de diseño que te dice como dees esrructurar una aplicacion, la aplicacion tiene muchos paquetes y destro de sto varos modulos sus componentes son:VISTAS<---Es donde se encontraran las interfaces, o atravez del menu de opcion (en consola), el usuario intereactua a travez de la vista con el sitema, el modelo intectua con la base de datos(mayormente), el controlador es lo que relaciona el objeto grafico con oyente (controlador)