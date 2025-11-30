from tkinter import *
def mostrarSeleccion():
    resultado.config(text=f"Opcion seleccionada: {opcion.get()}")

ventana=Tk()
ventana.geometry("500x500")
ventana.title("Radio Button")
opcion=StringVar()
radioBoton1=Radiobutton(ventana,text="Opcion 1",variable=opcion,value="Opcion1")
radioBoton1.pack()
radioBoton2=Radiobutton(ventana,text="Opcion 2",variable=opcion,value="Opcion2")
radioBoton2.pack()
radioBoton3=Radiobutton(ventana,text="Opcion 3",variable=opcion,value="Opcion3")
radioBoton3.pack()
boton=Button(ventana,text="Mostrar seleccion",command=mostrarSeleccion)
boton.pack()
resultado=Label(ventana)
resultado.pack()
ventana.mainloop()