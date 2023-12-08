"""""""""""""""""
Operadores lógicos
and, or, not, in, not in
"""""""""""""""""

a = 2
b = 3
# not inverte a expressão (o que é verdadeiro vira falso)
if not b>a:
    print('B é maior que A')

else:
    print('A é maior que B')

nome = 'Artur'

if 'Ar' not in nome:
    print ('não tem.')

else:
    print('tem.')


usuario = input('Qual seu nome? ')
senha = int(input('Qual sua senha? '))

usuario1 = 'Artur'
senha1 = 123

if usuario == usuario1 and senha == senha1:
    print('você está logado.')

else:
    print('inválido.')