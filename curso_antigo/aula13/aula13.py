"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
'''
variavel = 'Olá mundo'
print(variavel[::-1])

string1 = input('digite um nome: ')
string2 = input('digite outro nome: ')


print(f'A quantidade de caracteres digitados foi {len(string1) + len(string2)}')

'''
nome = input("Digite seu nome: ")
idade =input("Digite sua idade: ")

if nome == '' and idade == '':
    print('Você não digitou o nome ou idade')
else: 
    idade = int(idade)
    print(f'Seu nome é {nome} e você possui {idade} anos de idade')
    print(f'Seu nome tem {len(nome)} letras e invertido é {nome[::-1]}')
    print(f'A primeira letra do seu nome é "{nome[:1:1]}" e a última letra é "{nome[:-2:-1]}"')
    if ' ' in nome:
        print('Seu nome possui espaços vazios')
    else:
        print('Seu nome não possui espaços')