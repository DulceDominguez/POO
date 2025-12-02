from tkinter import *
from controler import funciones
from model import operaciones
from tkinter import messagebox

#EN VISTAS VA TODAS LAS INTERFACES, CADA TABKA ES UN ARCHIVO 
#Modificar la alerta de calcualdora para que diga :Deseas guardar en la base de datos 
#Crear una calculadora con :1.-Dos campos de texto 2.- 4 botones para las operaciones 3.- Mostrar el resultado en una alerta    
class Vistas:
    def __init__(self,ventana):
        ventana.title("Calculadorab Basica")
        ventana.geometry("1024x768")
        ventana.resizable(False,False)
        self.interfaz(ventana)
    def interfaz(self,ventana):
        #Campos de texto
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        num1=IntVar()
        txt_num1=Entry(ventana,textvariable=num1,width=5,justify="right")
        txt_num1.focus()
        txt_num1.pack(side="top",anchor="center",pady=7)
        
        num2=IntVar()
        txt_num2=Entry(ventana,textvariable=num2,width=5,justify="right")
        txt_num2.pack(side="top",anchor="center",pady=7)

        boton1=Button(ventana,text="Sumar",command=lambda:funciones.Controladores.operaciones("suma",num1.get(),num2.get(),"+"))
        boton1.pack(pady=7)

        boton2=Button(ventana,text="Restar",command=lambda:funciones.Controladores.operaciones("resta",num1.get(),num2.get(),"-"))
        boton2.pack(pady=7)

        boton3=Button(ventana,text="Multiplicar",command=lambda:funciones.Controladores.operaciones("multiplicacion",num1.get(),num2.get(),"x"))
        boton3.pack(pady=7)

        boton4=Button(ventana,text="Dividir",command=lambda:funciones.Controladores.operaciones("division",num1.get(),num2.get(),"/"))
        boton4.pack(pady=7)
    
        btn_salir=Button(ventana)
        lbl_resultado=Label(ventana)
        lbl_resultado.pack(pady=7)

    def menuPrincipal(self,ventana):
        menuBar=Menu(ventana)
        ventana.config(menu=menuBar)
        archivoMenu=Menu(menuBar,tearoff=False)
        menuBar.add_cascade(label="Operaciones",menu=archivoMenu)
        archivoMenu.add_command(label="Agregar",command=lambda:self.interfaz(ventana))
        archivoMenu.add_command(label="Consultar",command=lambda:self.consultar(ventana))
        archivoMenu.add_command(label="Cambiar",command=lambda:self.modificar(ventana))
        archivoMenu.add_command(label="Borrar",command=lambda:self.eliminar(ventana))
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir",command=ventana.quit)#Si manda parametros se debe poner otra cosa despues del commit 

    def eliminar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        lbl=Label(ventana,text=".:: Borrar una operacion ::.\n ")
        lbl.pack(pady=6)
        lbl_id=Label(ventana,text="ID de la Operacion: \n",justify="right")
        lbl_id.pack(pady=5,anchor="center")
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5,anchor="center")
        boton_eliminar=Button(ventana,text="Eliminar",command=lambda:funciones.Controladores.buscar(id.get()))
        boton_eliminar.pack(pady=5)

        boton_volver=Button(ventana,text="Volver",command=lambda:self.interfaz(ventana))
        boton_volver.pack(pady=5)
    
    def modificar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        lbl=Label(ventana,text=".:: Cambiar una operacion ::.\n ")
        lbl_id=Label(ventana,text="ID de la Operacion: \n",justify="right")
        lbl_id.pack(anchor="center",pady=7)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,width=5,justify="right")
        txt_id.focus()
        txt_id.pack(anchor="center",pady=7)
        lbl_num1=Label(ventana,text="Nuevo numero 1: \n",justify="right")
        lbl_num1.pack(anchor="center",pady=7)
        num1=IntVar()
        txt_num1=Entry(ventana,textvariable=num1,width=5,justify="right")
        txt_num1.pack(anchor="center",pady=7)
        lbl_num2=Label(ventana,text="Nuevo numero 2: \n",justify="right")
        lbl_num2.pack(anchor="center",pady=7)
        num2=IntVar()
        txt_num2=Entry(ventana,textvariable=num2,width=5,justify="right")
        txt_num2.pack(anchor="center",pady=7)
        lbl_signo=Label(ventana,text="Nuevo signo: \n",justify="right")
        lbl_signo.pack(anchor="center",pady=7)
        signo=StringVar()
        txt_signo=Entry(ventana,textvariable=signo,width=5,justify="right")
        txt_signo.pack(anchor="center",pady=7)
        lbl_resultado=Label(ventana,text="Nuevo resultado: \n",justify="right")
        lbl_resultado.pack(anchor="center",pady=7)
        resultado=DoubleVar()
        txt_resultado=Entry(ventana,textvariable=resultado,width=5,justify="right")
        txt_resultado.pack(pady=7,anchor="center")
        boton_guardar=Button(ventana,text="Guardar",command=lambda:funciones.Controladores.actualizar(id.get(),num1.get(),num2.get(),signo.get(),resultado.get()))
        boton_guardar.pack(pady=7)
        boton_volver=Button(ventana,text="Volver",command=lambda:self.interfaz(ventana))
        boton_volver.pack(pady=7)


    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def consultar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        lbl=Label(ventana,text=".:: Listado de operaciones ::.\n ")
        lbl.pack(pady=6)
        lista=funciones.Controladores.consultar()
        if len(lista)>0:
            for fila in lista:
                lbl_lista=Label(ventana)
                lbl_lista.config(text="")
                lbl_lista.config(text=f"Operacion {fila[0]} Fecha de creacion:{fila[1]}\n Operacion:{fila[2]}{fila[4]}{fila[3]}={fila[5]}")
                lbl_lista.pack()
        else:
            resultado=messagebox.showinfo(message="No hay registros en la base de datos",icon="info")

        boton_volver=Button(ventana,text="Volver",command=lambda:self.interfaz(ventana))
        boton_volver.pack(pady=5)
