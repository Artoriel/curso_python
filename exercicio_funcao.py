'''
def multi(*args):
    total = 0
    aux = 0
    for num in args:
        if num == 0:
            return 'Não pode haver 0.'
        else:
            aux = num
            total += num * aux
    return total

def parimpar(x):
    if x % 2 == 0:
        return f'{x} é par'
    
    return f'{x} é impar'
    
cont = 0
retornamulti = []

print("Digite dez valores.")
while cont < 11:
    ler = int(input("digite um número: "))
    retornamulti.append(ler)
    cont += 1

valor = multi(*retornamulti)
print(valor)

numero = input('Digite um número: ')
numero = int(numero)

resul = parimpar(numero)
print(resul)

'''

def retornanum(operacao):
    def multiplica(numero):
        r1 = numero * 2
        r2 = numero * 3
        r3 = numero * 4
        return f'{operacao} {numero} * 2  = {r1}, {operacao.lower()} {numero} * 3 = {r2} e {operacao.lower()} {numero} * 4 = {r3}'
    return multiplica



resultado = retornanum("A conta é")

num = input("Digite um número para ser duplicado, triplicado e quadruplicado: ")
num = int(num)

print(resultado(num))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))