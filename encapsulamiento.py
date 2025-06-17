class MiClase:
    def __init__(self):
        self._atributo_privado = 'valor'

    def _hablar(self):
        print(f'hola')

objeto = MiClase()
(objeto._hablar())