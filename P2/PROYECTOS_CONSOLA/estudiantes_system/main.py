from conexionBD import *
from estudiantes import estudianteBD
import os
class App:

    def _init__(self):
        self.main()

    def borrarPantalla(self):
        os.system("cls")

    def esperarTecla (self):
        input("Por favor oprima una tecal apra continuar")

    def datos_estudiante (self, tipo):
        print("..:: MENU DE ESTUDIANTE ::.")
        nombre=input("Ingrese el nombre del estudiante: ").strip().upper()
        nota=input("Ingrese la nota del estudiante: ").strip()
    def menu_acciones (self, tipo):#maestros,carrera
        print(f"\n\t\t.::  Menu de {tipo} ::.\n\t1.- Insertar \n\t2.- Consultar\n\t3.- Actualizar\n\t4.- Eliminar\n\t5.- Regresar ")
        opcion = input("\t\t Elige una opción: ").upper().strip()
        return opcion

    def respuesta_sql(self, respuesta):
        pass

    def menu_estudiante(self):
        opcion2=self.menu_acciones()
        if opcion2=="1":
            nombre,nota=self.datos_estudiante()
            alumno=estudianteBD.estudiante(nombre,nota)
            respuesta=alumno.insertar(nombre,nota)

        elif opcion2=="2":
            print
        elif opcion2=="3":
            print
        elif opcion2=="4":
            print
        elif opcion2=="5":
            print
    def main(self):
        opcion="1"
        while opcion!="4":
            opcion=input("\n\t\t ::: Menu Principal ::.\n\t 1.-Estudiante \n\t 2.-Salir \n\t Elige un opción: ").lower().strip()
            match opcion:
                case "1":
                    self.menu_estudiante()
                case "2":
                    self.borrarPantalla()
                    print("\n\t\t¡Gracias por utilizar el sistema!")
                    self.esperarTecla()
                case _:
                    input("\nOpcion invalidada ... vuelva a intertarlo ... ")    


if __name__=="__main__":
    app=App()
