class animal:
    def comer(self):
        print(f'el animal esta comiendo')

class ave(animal):
    def volar(self):
        print(f'el animal esta volando')

class mamifero(animal):
    def amamantar(self):
        print(f'el animal esta amamantando')

class murcielago(mamifero, ave):
    pass

MAMIFERO = mamifero()
MAMIFERO.comer()