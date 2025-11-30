
from conexionBD import *

class Nota:  
    @staticmethod
    def crear(usuario_id, titulo, descripcion):
      cursor.execute(
        "insert into notas values(%s,%s,%s,%s,NOW())",
        (usuario_id,usuario_id,titulo,descripcion) )
      conexion.commit()
      return True
       
      

    @staticmethod
    def mostrar(usuario_id):
        try:
          cursor.execute(
            "select * from notas where usuario_id=%s",
            (usuario_id,)
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(id, titulo, descripcion):
      cursor.execute(
        "update notas set titulo=%s,descripcion=%s where usuario_id=%s",
        (titulo,descripcion,id)
      )
      conexion.commit()
      return True
   
    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "delete from notas where id=%s",
            (id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
        
