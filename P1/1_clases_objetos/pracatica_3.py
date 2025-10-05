class Profesores:
    def __init__(self,num_profesor,experiencia,nombre):
        self.__num_profesor=num_profesor
        self.__experiencia=experiencia
        self.__nombre=nombre
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @property
    def num_profesor(self):
        return self.__num_profesor
    @num_profesor.setter
    def num2(self,num_profesor):
        self.__num_profesor=num_profesor
    @property
    def experiencia(self):
        return self.__experiencia
    @experiencia.setter
    def experiencia(self,experiencia):
        self.__experiencia=experiencia 
    def Impartir():
        return ("El maestro esta enseñando")
    def evaluar():
        return ("El maestro evaluo")   
Profesor1=Profesores(6,12,"Guadalupe")
Profesor2=Profesores(10,20,"Bertha")


class Alumnos:
    def __init__(self,nombre,matricula,edad):
        self.__nombre=nombre
        self.__matricula=matricula
        self.__edad=edad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def num2(self,matricula):
        self.__matricula=matricula
    @property
    def edad(self):
        return self.__edad
    @matricula.setter
    def edad(self,edad):
        self.__edad=edad
    def Incribirse():
        return ("El alumno esta inscrito")
    def estudiar():
        return ("El alumno esta estudiando")
alumnos1=Alumnos("Dulce","12345",18)
alumnos2=Alumnos("Jazmin","12345",20)


class Cursos:
    def __init__(self,creditos,nombre,codigo):
       self.__creditos=creditos
       self.__nombre=nombre
       self.__codigo=codigo
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @property
    def creditos(self):
        return self.__creditos
    @creditos.setter
    def creditos(self,creditos):
        self.__creditos=creditos
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo
    def asignar(self):
        return ("El alumno esta estudiando")
curso1=Cursos(5,"matematicas",566)
curso2=Cursos(6,"Filosofia",887)
