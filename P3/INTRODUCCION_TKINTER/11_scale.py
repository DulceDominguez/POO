from tkinter import *
ventana=Tk()
ventana.geometry("500x500")
ventana.title("Scale")
def mostrarEstado():
    resultado.config(text=f"Valor seleccionado por el usuario: {valor.get()}")
valor=IntVar()
escala=Scale(ventana,from_=0,to=100,orient='horizontal',variable=valor)
escala.pack()
boton=Button(ventana,text="Mostrar valor",command=mostrarEstado)
boton.pack()
resultado=Label(ventana)
resultado.pack()
ventana.mainloop()