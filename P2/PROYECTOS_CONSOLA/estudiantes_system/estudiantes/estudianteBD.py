from conexionBD import *
class Alumno:
    def __init__(self,nombre,nota):
        self.__nombre=nombre
        self.__nota=nota

    def insertar(self):
        try:
          cursor.execute(
            "insert into estudiantes values(null,%s,%s)",
            (self.__nombre,self.__nota)
          )
          conexion.commit()
          return True
        except:
          return False
    @staticmethod
    def consultar():
        try:
          cursor.execute(
            "select * from estudiantes"
          )
          return cursor.fetchall()
        except:    
          return []
    @staticmethod
    def actualizar(nombre,nota):
       try:
         cursor.execute(
            "update estudiantes set nombre=%s,nota=%s",
            (nombre,nota)
         )
         conexion.commit()
         return True
       except: 
         return False
    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "delete from estudiantes where id=%s",
            (id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False       