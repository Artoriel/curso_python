# Operadores relacionais
# == igual a
# > maior que
# >= maior que ou igual a
# < menor que
# <= menor que ou igual a
# != diferente de

nome = input('Qual o seu nome? ')
idade = int(input('Qual o sua idade? '))

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')

else:
    print(f'{nome} não pode pegar o empréstimo.')