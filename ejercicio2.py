class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f'nombre: {self.nombre}')
        print(f'edad: {self.edad}')
    

class Estudiante(persona):
    def __init__ (self, nombre, edad, grado):
     super().__init__(nombre, edad)
     self.grado = grado 

    def mostrar_grado(self):
        print(f'grado: {self.grado}')

estudiante = Estudiante('juan', '29', '2do')
estudiante.mostrar_datos()
estudiante.mostrar_grado()
