from abc import ABC, abstractclassmethod


class persona(ABC):
     @abstractclassmethod
     def __init__(self, nombre, edad, sexo, actividad):
          self.nombre = nombre
          self.edad = edad
          self.sexo = sexo
          self.actividad = actividad

     @abstractclassmethod
     def hacer_actividad(self):
      pass
          

     def presentarse(self):
         print(f'hola me llamo: {self.nombre} y tengo {self.edad} años')

class estudiante(persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'estoy estudiando {self.actividad}')

class trabajador(persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'actualmente estoy en el rubro de: {self.actividad}')

franco = estudiante('franco', 29, 'masculino', 'programacion')
loana = trabajador('loana', 30, 'femenino', 'DevOps')

loana.presentarse()
loana.hacer_actividad()
franco.presentarse()
franco.hacer_actividad()