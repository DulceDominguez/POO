from tkinter import *
from view import vista

class App:
    def __init__(self, ventana):
        view = vista.Vistas()
        view.interfaz(ventana)

if __name__ == "__main__":
    ventana = Tk()
    ventana.geometry("700x700")
    ventana.title("Sistema de Coches")
    app = App(ventana)
    ventana.mainloop()


"""
1 de diciembre
implementacion mvc
poo
interfaces:
3.1 menu principal *()
3.2 menu acciones *()
3.3 insertar autos()
3.4 consultar autos()
3.5 cambiar autos()
3.6 borrar autos()

productos entregables:
estructura del proyecto basado en mvc
modulo principal "main"
interaccion con las interfaces
nombre del commit: commit_01_12_25

3 de diciembre
3.7 insertar_camionetas
3.8 consultar_camionetas
3.9 cambiar_camionetas
3.10 borrar_camionetas
3.11 insertar_camiones
3.12 consultar_camiones
3.13 cambiar_camiones
3.14 borrar_camiones


productos entregables:
interaccion con todas las interfaces
nombre del commit: commit_03_12_25

4 de diciembre
controlador:
3.15 menu_principal 
3.16 menu_acciones 
3.17 insertar_autos 
3.18 consultar_autos 
3.19 cambiar_autos  
3.20 borrar_autos 

productos entregables:
interaccion con la funcionalidad (controlador) de las interfaces anteriores
nombre del commit: commit_04_12_25

"""