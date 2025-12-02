#Crear una calculadora con :1.-Dos campos de texto 2.- 4 botones para las operaciones 3.- Mostrar el resultado en una alerta    
from view import interfaz
from tkinter import *
class App():
    def __init__(self,ventana):
        view=interfaz.Vistas(ventana)
    
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()