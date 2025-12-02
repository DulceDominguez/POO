#1.-Paradigma OO 2.-implementar el MVC 3.-App de escritorio con interfaz grafica 
from tkinter import *
from view import vista
class App:
    def __init__(self,ventana):
        view=vista.Vistas(ventana)
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()