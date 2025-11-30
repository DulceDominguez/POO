from tkinter import *
from tkinter import messagebox
from model import coches
from view import vista

#CONTROLADOR COCHES
class Controlador_coches:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            mensaje=messagebox.showinfo(message=f"¡ Accion realizada con Éxito !",icon="info")
        else:
            mensaje=messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !",icon="info")
    
    @staticmethod
    def crear(marca,color,modelo,velocidad,caballaje,plazas):
        resultado=coches.Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
        Controlador_coches.respuesta_sql(resultado)

    @staticmethod
    def mostrar():
        registro=coches.Autos.consultar()
        return registro 
    
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,id):
        resultado=coches.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
        Controlador_coches.respuesta_sql(resultado)

    @staticmethod
    def eliminar(id):
        respuesta=coches.Autos.eliminar(id)
        Controlador_coches.respuesta_sql(id)

    @staticmethod
    def buscar(id):
        respuesta=coches.Autos.buscar(id)
        #try:
        if len(respuesta)>0:
            if respuesta:
                Controlador_coches.eliminar(id)
            else:
                mensaje=messagebox.showinfo(message=f"¡ hubo un error , vuelva a intentar por favor !",icon="info")
                return  
        else:
            mensaje=messagebox.showinfo(message=f"¡ La nota no existe , vuelva a intentar por favor !",icon="info")
            return
        
#CONTROLADOR CAMIONES        
class Controlador_camiones:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            mensaje=messagebox.showinfo(message=f"¡ Accion realizada con Éxito !",icon="info")
        else:
            mensaje=messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !",icon="info")

    @staticmethod
    def crear(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        resultado=coches.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
        Controlador_camiones.respuesta_sql(resultado)

    @staticmethod
    def mostrar():
        registro=coches.Camiones.consultar()
        return registro 
    
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id):
        resultado=coches.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
        Controlador_camiones.respuesta_sql(resultado)

    @staticmethod
    def eliminar(id):
        respuesta=coches.Camiones.eliminar(id)
        Controlador_camiones.respuesta_sql(id)

    @staticmethod
    def buscar(id):
        respuesta=coches.Camiones.buscar(id)
        #try:
        if len(respuesta)>0:
            if respuesta:
                Controlador_camiones.eliminar(id)
            else:
                mensaje=messagebox.showinfo(message=f"¡ Hubo un error , vuelva a intentar por favor !",icon="info")
                return  
        else:
            mensaje=messagebox.showinfo(message=f"¡ La nota no existe , vuelva a intentar por favor !",icon="info")
            return
        
#CONTROLADOR CAMIONETAS
class Controlador_camionetas:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            mensaje=messagebox.showinfo(message=f"¡ Accion realizada con Éxito !",icon="info")
        else:
            mensaje=messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !",icon="info")
    
    @staticmethod
    def crear(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        resultado=coches.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
        Controlador_camionetas.respuesta_sql(resultado)

    @staticmethod
    def mostrar():
        registro=coches.Camionetas.consultar()
        return registro 
    
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id):
        resultado=coches.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
        Controlador_camionetas.respuesta_sql(resultado)

    @staticmethod
    def eliminar(id):
        respuesta=coches.Camionetas.eliminar(id)
        Controlador_camionetas.respuesta_sql(id)
   



    