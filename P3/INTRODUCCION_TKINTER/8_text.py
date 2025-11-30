from tkinter import *
def comentario():
    comentario_obtenido=txt_comentario.get("1.0",END).strip()
    lbl_resultado.config(text=f"Comentario: {comentario_obtenido}")
ventana=Tk()
ventana.title("Uso de text")
ventana.geometry("600x400")
lbl_comentario=Label(ventana,text="Escriba su comentario: ").pack()#Si el elemento interactua no se pone pack
txt_comentario=Text(ventana)
txt_comentario.config(
    width=40,
    height=5,
    wrap="word"
)
txt_comentario.pack()
btn_comentario=Button(ventana,command=comentario,text="Mostrar comentario")
btn_comentario.pack()
lbl_resultado=Label(ventana,text="")
lbl_resultado.pack()

ventana.mainloop()