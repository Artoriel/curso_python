class Carro:
    def __init__(self, nome_carro):
        self.nome = nome_carro
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, nome_motor):
        self.nome_motor = nome_motor

    def carromotor(self):
        return f'{self.nome_motor}'
      
    

class Fabricante:
    def __init__(self, nome_fabricante):
        self.nome_fabricante = nome_fabricante

    def carromarca(self):
        return f'{self.nome_fabricante}'

fusca = Carro('Fusca')
motorfusca = Motor('1.2')
fusca.motor = motorfusca
print(fusca.nome, 'tem um motor', fusca.motor.carromotor())
Fabricantefusca = Fabricante('Volkswagen')
fusca.fabricante = Fabricantefusca
print(fusca.nome, 'tem um motor', fusca.motor.carromotor(), \
      'e é da marca',fusca.fabricante.carromarca())


