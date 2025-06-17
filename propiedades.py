class persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
     
    @property 
    def nombre(self):
        return self.__nombre
   
    @nombre.setter
    def nombre(self, new_nombre):
         self.__nombre = new_nombre

    @nombre.deleter 
    def nombre(self):
        del self.__nombre
   
   


franco = persona('francoo', '29')
nombre = franco.nombre
print(nombre)




franco.__nombre = 'pepe'

nombre = franco.__nombre
print(nombre)

del franco.nombre

print(nombre)