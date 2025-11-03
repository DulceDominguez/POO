from tkinter import *
#Ingresar el nombre con enrty , dar al boton de saludar y que abajo apresca hola y el nombre ingresado
def cambiar():
    nombre=txt_nombre.get()
    lbl_resultado.config(text=f"Bienvenid@...{nombre}")
ventana=Tk()
ventana.title("Entry")
ventana.geometry("500x500")
lbl_nombre=Label(ventana,text="Ingrese sun nombre: ").pack()
txt_nombre=Entry(ventana)
txt_nombre.pack()
btn_saludar=Button(ventana,text="Saludar",command=cambiar)
btn_saludar.pack()
lbl_resultado=Label(ventana,text="")
lbl_resultado.pack()
ventana.mainloop()