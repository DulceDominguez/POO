from tkinter import *
ventana=Tk()
ventana.geometry("800x600")
ventana.title("Marcos o frame en Tkinter")
#ventana.resizable(False,False)#Esto hace que no se pueda modificar el tamaño de la pantalla
marco1=Frame(ventana,width=600,height=400,bg="red", relief=SOLID,border=2)#relief="solid"
marco1.pack_propagate(False)#Evitar que se modifique el estilo del marco 1 para asi poder poner el marco 2 dentro de este 
marco1.pack(pady=150)#Es ñpara uwe se dibuje o muestre el objeto dentro de la ventana
marco2=Frame(marco1,width=300,height=150,bg="pink",relief=GROOVE,border=10).pack(pady=50)
ventana.mainloop()