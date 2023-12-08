'''''''''
operadores ternários
'''''''''


idade = input('Qual sua idade?')

if not idade.isnumeric():
    print('Voce precia digitar um número!')

else:
    idade = int(idade)
    e_de_maior = (idade >=18)
    msg= 'pode acessar' if e_de_maior else 'não pode acessar.'
    print(msg)