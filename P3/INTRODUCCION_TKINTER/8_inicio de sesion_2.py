from tkinter import *
#Ingresar el nombre con enrty , dar al boton de saludar y que abajo apresca hola y el nombre ingresado
#Boton de entrar y borrar,que abajo aparesca otra eit¿queta con el nombre, al momento de borrar que se elimine la etiqueta creada cuando se ingresa el nomrbe 
#Ingresar el nombre con enrty , dar al boton de saludar y que abajo apresca hola y el nombre ingresado
#pad y hacia bajo y pas x hacia os lados s
ventana=Tk()
ventana.title("Entry")
ventana.geometry("800x600")
lbl_titulo=Label(ventana,text="Inicio de sesion")
lbl_titulo.config(
        fg="#EC8DFF",
        bg="#FFAAF8",
        width=50,
        height=2,
        font=("Arial",20,"bold"),
        relief=GROOVE,
        border=2)
lbl_titulo.pack()
marco=Frame(ventana)
marco.config(
        width=800,
        height=300,
        bg="silver"
)
marco.pack_propagate(False)
marco.pack()
lbl_nombre=Label(ventana,text="Ingrese su nombre: ").pack()
lbl_nombre.grid(pady=5,padx=5)
nombre=StringVar()
txt_nombre=Entry(ventana,textvariable=nombre)



















