class F():
    def __init__(self):
        self.E = 'soy el Padre'
    def hablar(self):
        print('hola {self.E}')


class E(F):
    def __init__(self):
      super().__init__()
      self.C = 'y yo soy el hijo'
    def hablar(self):
        print(f'Hola {self.E} {self.C}')
    
class A():
    pass

class a(A):
    pass

class b(a):
    def hablar(self):
        print('hola habla b')

class d(E):
    pass

class c(d):
    pass

class d(b, c):
    pass


b.hablar()

print(d.mro())

