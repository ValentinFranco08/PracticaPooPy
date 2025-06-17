class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f'estas haciendo una llamada desde un {self.modelo}') 
    
    def cortar(self):
        print(f'cortaste la llamada desde tu {self.modelo}')


celular1 = Celular('samsung', 's23 ultra', '200mpx')
celular2 = Celular('Apple', 'iphone 15 pro', '200mpx')

celular1.cortar()