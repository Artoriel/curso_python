# Contador e acumulador
"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
'''
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador  = acumulador + contador
    contador += 1
else:
    print('chegou no else!')

print('acabou.')


contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')
'''

string1 = input("String: ")
cont = 0
novastring = ''
while cont < len(string1):
    print(string1[cont])
    letra = string1[cont]
    novastring += f'*{letra}'
    cont = cont + 1
    
   
print('cabo')
print(novastring)


frase = 'aaaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)



