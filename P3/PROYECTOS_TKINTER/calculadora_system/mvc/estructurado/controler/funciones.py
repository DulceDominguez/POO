from tkinter import messagebox
def sumar(numero1,numero2):
    suma=numero1+numero2
    resultado=messagebox.showinfo(message=f"{numero1}+ {numero2}={suma}",icon="info",title="Sumar")
def restar(numero1,numero2):
    resta=numero1-numero2
    resultado=messagebox.showinfo(message=f"{numero1}-{numero2}={resta}",icon="info",title="Restar")
def dividir(numero1,numero2):
    div=numero1/numero2
    resultado=messagebox.showinfo(message=f"{numero1}/{numero2}={div}",icon="info",title="Dividir")
def multi(numero1,numero2):
    multi=numero1*numero2
    resultado=messagebox.showinfo(message=f"{numero1}x{numero2}={multi}",icon="info",title="Multiplicacion")