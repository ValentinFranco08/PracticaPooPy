class persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre
   
    def set_nombre(self, new_nombre):
         self._nombre = new_nombre


franco = persona('franco', '29')
nombre = franco.get_nombre()
print(nombre)

franco.set_nombre('franquito')


franco1 = franco.get_nombre()
print(franco1)