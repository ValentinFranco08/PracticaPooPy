class Estudiante:
     def __init__(self, Nombre, Edad, Grado):
          self.Nombre = Nombre
          self.Edad = Edad
          self.Grado = Grado

     def Estudiar(self):
          print('estudiando ...')


Nombre = input('digame su nombre ')
Edad = input('Digame su edad ')
Grado = input('digame su grado ')

estudiante = Estudiante(Nombre, Edad, Grado)

print(f'''
      datos del estudiante: 
      Nombre: {estudiante.Nombre}
      Edad: {estudiante.Edad}
      Grado: {estudiante.Grado} 
     
''')
while True:
 estudiar = input()
 if (estudiar.lower() == 'estudiar'):
    estudiante.Estudiar()