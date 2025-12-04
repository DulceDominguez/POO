from tkinter import messagebox
from model import operaciones
class Controladores:
    @staticmethod
    def operaciones(titulo,num1,num2,signo):
        if signo=="-":
            resultado=num1-num2
        elif signo=="+":
            resultado=num1+num2
        elif signo=="x":
            resultado=num1*num2
        elif signo=="/":
            resultado=num1/num2
        resul=messagebox.askquestion(title=titulo,message=f"\t\t{num1}{signo}{num2}={resultado}\n\n¿Desea guardar la operacion en la base de datos?",icon="question")
        if resul=="no":
            pass
        elif resul=="yes":
            respuesta=operaciones.Operaciones.crear(num1,num2,signo,resultado)
            Controladores.respuesta_sql("Agregar registro",respuesta)
    
    @staticmethod
    def actualizar(id,num1,num2,signo,resultado):
        resul=messagebox.askquestion(title="Confimacion de actualizar",message=f"¿Desea realmetne modificar el registro de la base de datos?",icon="question")
        if resul:
            respuesta=operaciones.Operaciones.actualizar(id,num1,num2,signo,resultado)
            Controladores.respuesta_sql("Actualizar registro",respuesta)

    @staticmethod        
    def eliminar(id):
        resul=messagebox.askquestion(title="Confimacion de eliminar",message=f"¿Desea eliminar la operacion en la base de datos?",icon="question")
        if resul=="yes":
            respuesta=operaciones.Operaciones.eliminar(id)
            if respuesta:
                mensaje=messagebox.showinfo(message=f"¡ Accion realizada con Éxito !",icon="info")
            else:
                mensaje=messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !",icon="info")
         
    @staticmethod
    def consultar():
        lista=operaciones.Operaciones.mostrar()
        return lista

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            mensaje=messagebox.showinfo(message=f"¡ Accion realizada con Éxito !",icon="info")
        else:
            mensaje=messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !",icon="info")
    @staticmethod
    def buscar(id):
        respuesta=operaciones.Operaciones.buscar(id)
        #try:
        if len(respuesta)>0:
            if respuesta:
                Controladores.eliminar(id)
            else:
                mensaje=messagebox.showinfo(message=f"¡ hubo un error , vuelva a intentar por favor !",icon="info")
                return  
        else:
            mensaje=messagebox.showinfo(message=f"¡ La nota no existe , vuelva a intentar por favor !",icon="info")
            return
            
                
        #except TypeError:
            
        
    