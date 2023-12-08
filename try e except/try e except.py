try:
    a = 1/0
except NameError as erro:
    print('Erro do dev.')
except Exception as erro:
    print('Ta errada essa parada.')
else:
    pass
finally:
    a = 'aaa'

print(a)


def divide(n1,n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return n1/n2

try:
    print(divide(2,0))
except ValueError as error:
    print("Não se divide por zero")
    print('Log:', error)

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
         pass


while True:
    numero = converte_numero(input('Digite um número: '))

    if numero is None:
        print("Erro, isso não é número")
    else:
        print(numero *2)




