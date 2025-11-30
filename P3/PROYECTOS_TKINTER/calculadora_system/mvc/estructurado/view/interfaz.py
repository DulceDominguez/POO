from tkinter import *
from controler import funciones
#Crear una calculadora con :1.-Dos campos de texto 2.- 4 botones para las operaciones 3.- Mostrar el resultado en una alerta    
def interfaz():
    ventana=Tk()
    ventana.title("Calculadorab Basica")
    ventana.geometry("800x600")
    ventana.resizable(False,False)
    #Campos de texto
    num1=IntVar()
    txt_num1=Entry(ventana,textvariable=num1,width=5,justify="right")
    txt_num1.pack(side="top",anchor="center")
    
    num2=IntVar()
    txt_num2=Entry(ventana,textvariable=num2,width=5,justify="right")
    txt_num2.pack(side="top",anchor="center")

    boton1=Button(ventana,text="Sumar",command=lambda:funciones.sumar(num1.get(),num2.get()))
    boton1.pack()

    boton2=Button(ventana,text="Restar",command=lambda:funciones.restar(num1.get(),num2.get()))
    boton2.pack()

    boton3=Button(ventana,text="Multiplicar",command=lambda:funciones.multi(num1.get(),num2.get()))
    boton3.pack()

    boton4=Button(ventana,text="Dividir",command=lambda:funciones.dividir(num1.get(),num2.get()))
    boton4.pack()
 
    btn_salir=Button(ventana)
    lbl_resultado=Label(ventana)
    lbl_resultado.pack()

    ventana.mainloop()