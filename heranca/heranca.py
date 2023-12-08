class Pessoa:
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando')
    def falar(self):
        print('CLIENTE')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} está estudando')

class Clientevip(Cliente):
    def __init__(self, idade, nome, sobrenome):
        Pessoa.__init__(self, idade, nome)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')




p1 = Pessoa(45, 'Jorge')
p1.falar()

c1 = Cliente(23, 'Arthur')
c1.comprar()

c2 = Clientevip(47, "Joao", "Marston")
c2.falar()
