#controlador-validacion
from tkinter import *
from tkinter import messagebox
from model import usuario,nota
from view import vista
class Controlador:
    @staticmethod
    def mostrar(id):
        registro=nota.Nota.mostrar(id)
        return registro 

    @staticmethod
    def registrar(nombre,apellidos,email,password):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        Controlador.respuesta_sql(resultado)

    @staticmethod
    def login(email,password,ventana):
        registro=usuario.Usuario.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(icon="info", message=f"{registro[1]}{registro[2]} Haz iniciado sesion correctamente {email}")
            vista.Vistas.menu_notas(ventana,registro[0],registro[1],registro[2])
        else:
            messagebox.showinfo(icon="info", message=f"Credenciales incorrectas, por favor intenta de nuevo")

    @staticmethod
    def crear(id,titulo,descripcion):
        resultado=nota.Nota.crear(id,titulo,descripcion)
        Controlador.respuesta_sql(resultado)

    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            mensaje=messagebox.showinfo(message=f"¡ Accion realizada con Éxito !",icon="info")
        else:
            mensaje=messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !",icon="info")
    
    @staticmethod
    def eliminar(id_nota):
        resul=messagebox.askquestion(title="Confimacion de eliminar",message=f"¿Desea eliminar la operacion en la base de datos?",icon="question")
        if resul=="yes":
            resultado=nota.Nota.eliminar(id_nota)
            Controlador.respuesta_sql(resultado)
        else:
            return

    @staticmethod
    def actualizar(id_nota,t,d):
        resultado=nota.Nota.actualizar(id_nota,t,d)
        Controlador.respuesta_sql(resultado)

