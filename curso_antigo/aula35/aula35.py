

def vazia(arg):
    print(arg)

def algo():
    outra_mensagem = "olá"
    return outra_mensagem



variavel = algo()
vazia(variavel)


def primeira_palavra(nome):
    return f"Olá {nome},"

def segunda_palavra(palavra2, palavra3):
    return f"{palavra2} {palavra3}?"

def recebe(v1,v2):
    print(v1,v2)

var1 = primeira_palavra('Artur')
var2 = segunda_palavra('como','esta')

print(recebe(var1,var2))

