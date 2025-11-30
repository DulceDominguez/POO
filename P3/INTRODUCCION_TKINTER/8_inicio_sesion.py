from tkinter import *
#Ingresar el nombre con enrty , dar al boton de saludar y que abajo apresca hola y el nombre ingresado
#Boton de entrar y borrar,que abajo aparesca otra eit¿queta con el nombre, al momento de borrar que se elimine la etiqueta creada cuando se ingresa el nomrbe 
#Ingresar el nombre con enrty , dar al boton de saludar y que abajo apresca hola y el nombre ingresado
ventana=Tk()
ventana.title("Entry")
ventana.geometry("500x500")
def entrar():
    nombre=txt_nombre.get()
    lbl_resultado.config(
        text=f"Bienvenid@...{nombre}",
        bg="#000000",
        width=50,
        height=2,
        font=("Arial",20,"bold"),
        relief=GROOVE,
        border=2
        )

def borrar():
    txt_nombre.delete(0,END)
    txt_contrasenia.delete(0,END)
    txt_nombre.focus()
    color_defecto=ventana.cget("bg")
    #txt_nombre.destroy()
    lbl_resultado.config(
        text="",
        bg=color_defecto,
        border=0

    )

def salir():
    ventana.quit()#Se quita pero no se sale completamentepero lo correcto seria exit
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
nombre=StringVar()
lbl_nombre=Label(ventana,text="Ingrese su nombre: ").pack()
txt_nombre=Entry(ventana,textvariable=nombre)
#txt_nombre.config(state="readonly")#disabled no deja seleccionar la caja de texto 
txt_nombre.focus()
txt_nombre.pack()
password=StringVar()
lbl_contrasenia=Label(ventana,text="Ingrese su contraseña: ").pack()
txt_contrasenia=Entry(ventana,textvariable=password,show="*")
txt_contrasenia.pack()
btn_entrar=Button(ventana,text="Entrar",command=entrar)
btn_entrar.pack()
btn_borrar=Button(ventana,text="Borrar",command=borrar)
btn_borrar.pack()
btn_salir=Button(ventana,text="Salir",command=salir)
btn_salir.pack()
lbl_resultado=Label(ventana,text="")
lbl_resultado.pack()
ventana.mainloop()
