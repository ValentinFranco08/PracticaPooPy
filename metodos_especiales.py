class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def __str__(self):
         return f'persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
         return f'persona({self.nombre}, {self.edad})'
    
    def  __add__(self, otro):
         nuevo_valor = self.edad + otro.edad
         return persona(self.nombre+otro.nombre, nuevo_valor)

franco = persona('franco', 29)
julieta = persona('julieta', 25)
gustavo = persona('gustavo', 35)


#repre = repr(franco)
#resultado = eval(repre)
#print(resultado.nombre)

nueva_persona = franco+julieta+gustavo
print(nueva_persona.nombre)