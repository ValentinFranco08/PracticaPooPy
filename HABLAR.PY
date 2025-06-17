

class a():
    def hablar1(self):
        print('soy a ')

class b(a):
    pass

class c(a):
    pass

class d(b,c):
    def hablar(self):
        pass



D = d()
D.hablar()