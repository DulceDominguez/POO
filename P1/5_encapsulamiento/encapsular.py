#ENCAPSULAMIENTO:Es un pilar de la POO que permite indicar cual es la manera de como poder utilizar los atributos y metodos de una clase a la hora de usar en objetos o en herencia, si no heredo no tiene sentido en encapsulamiento
class clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy atributo privado"

    def __init__(self,color,tamaño):
        self.__color=color
        self.__tamaño=tamaño

    property
    def Color(self):#<--Get
        return self.color
    
    Color.setter
    def Color(self,color):
        self._color=color
    
    property
    def Tamano(self):#<--Get
        return self._tamaño
    
    Tamano.setter
    def Color(self,tam):
        self._tamaño=tam
    
    property
    @atributo_publico
    def atributopublico(self):
        self.atributo_publico
    
    @atributo_publico.setter
    def atributopublico(self,atributo_publico):
            self.atributo_publico=atributo_publico
        
    property
    @_atributo_protegido
    def atributo_publico(self):
        self._atributo_protegido
    @_atributo_protegido.setter
    def _atributo_protegido(self,_atributo_protegido):
            self._atributo_protegido=_atributo_protegido
    
    property
    @__atributo_privado
    def atributo__privado(self):
        self.__atributo_privado
    @_atributo_protegido.setter
    def __atributo_privado(self,__atributo_privado):
            self.__atributo_privado=__atributo_privado


    def Get_Atributo_Privado(self):
        return self.__atributo_privado
#Tener un constructor implica enviar siempre los argumentos que estan como parametros despues de self
#Los que no estan en constructor se crean hasta el momento que se invocan 
#No es una buena practica acceder a los valores directamente, sino atravez de un metodo(get)
objeto=clase("Rojo","Grande")
print(objeto.atributo_publico)
print(objeto.Get_Atributo_Privado())


