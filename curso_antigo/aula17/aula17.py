'''''''''
formatar valores

:s - texto (strings)
:d - inteiros (int)
:f - float 

:.(Numero)f  - quantidade de casas decimais (float)
:(CARACTERES)(<,>,^) (QUANTIDADE)(TIPO - s,d ou f)

> - esquerda
< - direito
^ - centro
'''''''''

num1 = 1250
print(f'{num1:0>10}')
num2 = 1
num3 = 5
divisao = 1/5
print('{:.2f}'.format(divisao))

nome = 'Artur'
sobrenome = 'Smaniotto'
nomeformatado = '{0:#^10}' .format(nome, sobrenome)
print(nomeformatado)

print(nome.lower()) # tudo minúsculo
print(nome.upper()) # tudo maiusculo
print(nome.title()) # somente primeiras letras maiusculas