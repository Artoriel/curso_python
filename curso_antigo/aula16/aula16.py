numero_inteiro = input('Digite um número: ')


if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é par.')

    else:
        print(f'{numero_inteiro} é ímpar.')


else:
    print('Esse não é um número inteiro!')





horario = int(input('digite um horário: '))

if horario > 0 and horario <11:
   print('bom dia!')

elif horario >12 and horario < 17:
    print('Boa tarde!')

elif horario > 18 and horario < 23:
    print('Boa noite!')

else:
   print()



usuario = input('Digite seu nome: ')

if len(usuario) <= 4:
    print('Seu nome é curto.')

elif len(usuario) == 5 or len(usuario) == 6:
    print('Seu nome é normal')

elif len(usuario) > 6:
    print('seu nome é grande.')

else:
    print()