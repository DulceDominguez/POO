from tkinter import *
from tkinter import ttk
import os
ventana=Tk()
ventana.geometry("500x500")
ventana.title("Imagenes con  pillow")
def mensaje(tipo):
    resultado.config(text=tipo)
# Obtener la ruta absoluta del directorio donde está este archivo .py
ruta_base = os.path.dirname(os.path.abspath(__file__))
print(ruta_base)
# Construir la ruta completa al archivo de imagen
ruta_imagen = os.path.join(ruta_base, "logo.png")
print(ruta_imagen)
#Primer manera de agregar imagenes con la libreria de tkinter
#FotoImage solo permite archivos con extension .png  .gift ,pgm/.ppm
imagen=PhotoImage(file=ruta_imagen)
#Incluir o mostrar la imagen dentro de un label o button
etiqueta=Label(ventana,image=imagen)
etiqueta.pack()
boton=Button(ventana,image=imagen,command=lambda:mensaje("Hola python"))
resultado=Label(ventana,text="")
resultado.pack()
ventana.mainloop()