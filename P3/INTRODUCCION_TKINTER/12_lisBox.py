from tkinter import *
ventana=Tk()
ventana.geometry("500x500")
ventana.title("List Box")
def mostrarSeleccion():
    seleccion=lista.get(lista.curselection())#curselection es la opcion seleccionada
    resultado.config(text=f"Seleccionaste: {seleccion}")
lista=Listbox(ventana,width=10,height=5,selectmode='single')
lista.pack()
opciones=['Amarillo','Rojo','Azul','Morado']
for i in opciones:
    lista.insert(END,i)
boton=Button(ventana,text="Mostrar seleccion del usuario",command=mostrarSeleccion)
boton.pack()
resultado=Label(ventana,text="")
resultado.pack()
ventana.mainloop()