from tkinter import *
def mostrarResultado(opcion):
    resultado.config(text=f"{opcion}")
ventana=Tk()
ventana.geometry("500x500")
ventana.title("Menu")
menuBar=Menu(ventana)
ventana.config(menu=menuBar)#editar:copiar-recortar y salir
archivoMenu=Menu(menuBar,tearoff=False)
menuBar.add_cascade(label="Archivo",menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo",command=lambda:mostrarResultado("Nuevo Archivo"))
archivoMenu.add_command(label="Guardar Archivo",command=lambda:mostrarResultado("Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=ventana.quit)#Si manda parametros se debe poner otra cosa despues del commit 
#EDITAR
editarMenu=Menu(menuBar,tearoff=False)
menuBar.add_cascade(label="Edicion",menu=editarMenu)
editarMenu.add_command(label="Copiar",command=lambda:mostrarResultado("Copiar"))
editarMenu.add_command(label="Recortar",command=lambda:mostrarResultado("Recortar"))
editarMenu.add_separator()
editarMenu.add_command(label="Salir",command=ventana.quit)#Si manda parametros se debe poner otra cosa despues del commit 
resultado=Label(ventana,text="")
resultado.pack()
ventana.mainloop()