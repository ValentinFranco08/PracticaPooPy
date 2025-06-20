class personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza 
        self.velocidad = velocidad 


    def __repr__ (self):
        return f'{self.nombre}, (fuerza: {self.fuerza}, velocidad: {self.velocidad})'
    
 
155    def __add__ (self, otro_pj):
        nuevo_nombre = self.nombre + '-' + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.5)
        nueva_velocidad = round (((self.velocidad + otro_pj.velocidad)/2)**1.5)
        return personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
     
Ryoma = personaje('Ryoma', 100, 100)
Goku = personaje('Goku', 150, 150)
Vegeta = personaje('Vegeta', 200, 200)
Ryogoku = Ryoma + Goku
Vegryku = Ryogoku + Vegeta
print(Vegryku)
print(Ryogoku)
print(Ryoma)
print(Goku)
print(Vegeta)