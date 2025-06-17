class Animal:
    def sonido(self):
        pass

class Gato:
    def sonido(self):
        return 'miau'
    
class Perro:
    def sonido(self):
        return 'guauu'
    
def hacer_sonido(animal):
    print(animal.sonido())   


gato = Gato()
perro = Perro()

hacer_sonido(perro)

print(gato.sonido())