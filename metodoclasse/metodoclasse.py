from random import randint


class Pessoa:
    ano_atual = 2019

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(1000,2000)
        return rand



p1 = Pessoa('Arthur', 18)


print(p1.gera_id())