from tkinter import *
#Que cuendo se le click en el primer boton se cambie el colo r de la etiqueta superoor cambie y ca,bie le texto a poo con python
ventana=Tk()
ventana.title("Personalizar widgets u objetos")
ventana.geometry("500x500")
etiqueta=Label(ventana,text="Bienvenidos a Tkinter")
etiqueta.config(
    bg="blue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"Italic"),
    border=2,
    relief="raised"
    )
etiqueta.pack(pady=25)
boton1=Button(ventana,text="Bienvenidos a Tkinter")
boton1.config(
    #bg="blue",
    fg="white",
    width=15,
    font=("Arial",20,"bold"),
    border=2,
    relief=GROOVE,
    activeforeground="yellow",
    activebackground="red"
    )
etiqueta.pack(pady=25)
ventana.mainloop()