from tkinter import *
def RecibirNoti():
    if opcion.get()==1:
        resultado.config(text=f"Las notificaiones estan activadas")
    else:
        resultado.config(text=f"Las notificaiones estan desactivadas")
ventana=Tk()
ventana.geometry("500x500")
ventana.title("Check Button")
opcion=IntVar()
checkBoton=Checkbutton(ventana,text="Deseas activar las notificaciones?",variable=opcion,onvalue=1,offvalue=0)
checkBoton.pack()
boton=Button(ventana,text="Confirmar",command=RecibirNoti)
boton.pack()
resultado=Label(ventana,text="")
resultado.pack()
ventana.mainloop()