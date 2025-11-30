from tkinter import *
#Que cuendo se le click en el primer boton se cambie el colo r de la etiqueta superoor cambie y ca,bie le texto a poo con python
ventana=Tk()
ventana.title("Distibucion de widgets en pantalla")
ventana.geometry("600x400")
#OPCION 1:Usar pack con side =LEFT O RIGHT,con ancor o ancor 
Label(ventana,text="Nombre: ").pack(anchor="nw",side="top",padx=5,pady=5)#En autamatico con pack lo pone centrado
#anchor es con norte,sur...el padx y y es dcon el plano cartesiano
Entry(ventana).pack(anchor="nw",side="top",padx=5,pady=5)
Label(ventana,text="Contraseña: ").pack(anchor="nw",side="top",padx=5,pady=5)#En autamatico con pack lo pone centrado
Entry(ventana).pack(anchor="nw",side="top",padx=5,pady=5)
#Si no se crean los elementos con objetosen un futuro es mas dificil reutilizarlo a menos que sea con textvariable y modificar la variable asignada a textvariabñe 
#OPCION 2:Usar grid
Label(ventana,text="Nombre: ").grid(row=0,column=0,padx=5,pady=5)#Se puede usar side 
Entry(ventana).grid(row=0,column=1,padx=5,pady=5)
Label(ventana,text="Contraseña: ").grid(row=1,column=0,padx=5,pady=5)#En autamatico con pack lo pone centrado
Entry(ventana).grid(row=0,column=0,padx=5,pady=5)
ventana.mainloop()
