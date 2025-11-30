from tkinter import *
from tkinter import messagebox
#Crear una calculadora con :1.-Dos campos de texto 2.- 4 botones para las operaciones 3.- Mostrar el resultado en una alerta    
ventana=Tk()
ventana.title("Calculadora")
ventana.geometry("800x600")
ventana.resizable(False,False)

def operaciones(tipo,numero1,numero2):
    if tipo=="suma":
        suma=numero1+numero2
        resultado=messagebox.showinfo(message=f"{numero1}+ {numero2}={suma}",icon="info",title="Sumar")
    elif tipo=="resta":
        resta=numero1-numero2
        resultado=messagebox.showinfo(message=f"{numero1}-{numero2}={resta}",icon="info",title="Restar")
    elif tipo=="multi":
        multi=numero1*numero2
        resultado=messagebox.showinfo(message=f"{numero1}x{numero2}={multi}",icon="info",title="Multiplicacion")
    elif tipo=="div":
        div=numero1/numero2
        resultado=messagebox.showinfo(message=f"{numero1}/{numero2}={div}",icon="info",title="Dividir")

num1=IntVar()
txt_num1=Entry(ventana,textvariable=num1,width=5,justify="right")
txt_num1.pack(side="top",anchor="center")
num2=IntVar()
txt_num2=Entry(ventana,textvariable=num2,width=5,justify="right")
txt_num2.pack(side="top",anchor="center")

boton1=Button(ventana,text="Sumar",command=lambda:operaciones("suma",num1.get(),num2.get()))
boton1.pack()

boton2=Button(ventana,text="Restar",command=lambda:operaciones("resta",num1.get(),num2.get()))
boton2.pack()

boton3=Button(ventana,text="Multiplicar",command=lambda:operaciones("multi",num1.get(),num2.get()))
boton3.pack()

boton4=Button(ventana,text="Dividir",command=lambda:operaciones("div",num1.get(),num2.get()))
boton4.pack()
 
btn_salir=Button(ventana)
lbl_resultado=Label(ventana)
lbl_resultado.pack()

ventana.mainloop()