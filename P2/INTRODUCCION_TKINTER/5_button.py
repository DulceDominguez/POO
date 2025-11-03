from tkinter import *
def cambiarTexto():
    nombre.config(text="Dulce Dominguez Avila")
    contrasenia.config(text="5678")
def regresarTexto():
    nombre.config(text="Nombre: ")
    contrasenia.config(text="Contraseña: ")
ventana=Tk()
ventana.title("Uso del botones,marcos y etiquetas ")
ventana.geometry("800x600")
marco1=Frame(ventana)
marco1.config(
    width=800,
    height=50,
    bg="#BAF4FF",
    border=2,
    relief="raised")
marco1.pack_propagate(False)
marco1.pack(pady=10)
#Crear etiquetas
titulo=Label(marco1,text="Inicio de sesion: ", bg="#BAF4FF").pack(pady=10)
nombre=Label(ventana,text="Nombre: ")
nombre.pack(pady=10)
contrasenia=Label(ventana,text="Contaseña: ")
contrasenia.pack(pady=10)
boton=Button(ventana,text="Aceptar",command=cambiarTexto).pack(pady=10)
boton2=Button(ventana,text="Regresar",command=regresarTexto).pack(pady=10)
ventana.mainloop()