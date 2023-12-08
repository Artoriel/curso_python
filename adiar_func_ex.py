# Exercício - Adiando execução de funções

def criar_funcao(operecao):
    def multiplica_ou_soma(x,y):
        if operecao == '+':
            return x + y
        if operecao == '*':
            return x * y
        return f'"{operecao}" desconhecido'
    return multiplica_ou_soma

op = input('Qual operação você quer? ')
soma_com_cinco = criar_funcao(op)
print(soma_com_cinco(2,4))

# multiplica_por_dez = criar_funcao(multiplica, 10)

# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))