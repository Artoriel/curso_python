'''
entrada = input('Digite um número: ')
try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
'''

hora = input("Que horas são?")


if hora.isdigit():
    hora_int = int(hora)
    bom_dia = hora_int >= 0 and hora_int <=11
    boa_tarde = hora_int >=12 and hora_int <=17
    boa_noite = hora_int >=18 and hora_int <=23
    if bom_dia:
        print("Bom dia")
    elif boa_tarde:
        print("Boa tarde")
    elif boa_noite:
        print("Boa noite")
    else:
        print("hora desconhecida")
else:
    print("nao é int")


nome = input("Qual seu nome?")

if len(nome) <4 :
    print('nome curto')
elif len(nome) > 5 and len(nome) <=6:
    print('seu nome é normal')
else:
    print('seu nome é grande')
