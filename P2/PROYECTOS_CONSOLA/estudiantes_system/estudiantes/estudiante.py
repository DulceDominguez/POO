#Realizar un programa que conste de una clase llamada estudiante que tenga como atributos el nombre y la nota del alumno.Definir los metodos para inicializar sus atributos,imprimirlos y motrar un mensaje con el resultado de la nota y si ha aprobado o no
from conexionBD import *
class Estudiantes:
    def __init__(self,nombre,nota):
        self.__nombre=nombre
        self.__nota=nota
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self,nota):
        self.__nota=nota
    
    def aprovado(self):
        if self.__nota>7:
            return "aprobado"
        elif self.__nota<7:
            return "desaprobado"
    
    @staticmethod
    def insertar(nombre,nota):
        try:
            cursor.execute(
                "insert into estudiante values(null,%s,%s)",
                (nombre,nota)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def mostrar():
        try:
          cursor.execute(
            "select * from estudiante")
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(id,nombre,nota):
       try:
         cursor.execute(
            "update estudiante set nombre=%s,nota=%s where id=%s",
            (nombre,nota,id))
         conexion.commit()
         return True
       except: 
         return False
    
    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "delete from estudiante where id=%s",
            (id,)) 
          conexion.commit() 
          return True  
        except:    
          return False
        





    