class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def __str__(self):
         return f'persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
         return f'persona({self.nombre}, {self.edad})'
    

franco = persona('franco', 29)


repre = repr(franco)
resultado = eval(repre)
print(resultado.nombre)