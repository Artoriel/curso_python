
import random
# def deltaf(a,b,c):
#     def baskara():
#         delta = (b**2) - (4*a*c)
#         x1 = (-b + delta ** (1/2))/ (2*a)
#         x2 = (-b - delta ** (1/2))/ (2*a)
#         if delta < 0:
#             return 'Não há raiz'
#         if delta == 0:
#             return f'As raízes são iguais: {round(x1, 2)} e {round(x2,2)}'
#         return f'As raízes são {round(x1, 2)} e {round(x2, 2)}'
#     return baskara

# a = float(input('Digite o valor de a: '))
# b = float(input('Digite o valor de b: '))
# c = float(input('Digite o valor de c: '))
# baskara =  deltaf(a,b,c)
# print(baskara())


# def somalista(lista):
#     soma = 0
#     for num in lista:
#         try:
#             soma += num
#         except TypeError:
#             return 'Valor invalido'
#     return soma
    

# lista = [1,'a',3,8,5,6]
# print(somalista(lista))
# lista = []
# cont = 0
# dife = 0
# maior = 0
# while cont < 10:
#     num = input('Digite um número: ')
#     lista.append(float(num))
#     cont += 1

# cont = 0
# while cont + 1 < len(lista):
#     dife = lista[cont] - lista[cont + 1]
#     if dife < 0:
#         dife *= -1
#     if dife > maior:
#         maior = dife

#     cont +=1

# print(maior)
# from collections import Counter

# lista = [1,1,6,'f',4,4,6,5,1, 'f']
# for obj, vezes in Counter(lista).items():
#     print(f'{obj} aparece {vezes} vez(es)')

# alternativas = ['A', 'B', 'C', 'D', 'E']
# gabarito = ['B', 'C', 'A', 'D', 'B', 'B', 'E', 'C',
# 'A', 'B', 'D', 'A', 'A', 'A', 'A','B', 'D', 'C', 'E', 'E', 'A', 'C', 'E', 'D' ,'B']
# cont = 0
# acertos = 0
# while cont < len(gabarito):
#     resp = input('Digite uma alternativa: ').upper()

#     if resp not in alternativas:
#         print('Alternativa inválida, tente novamente')
#         continue

#     if (resp == gabarito[cont]):
#         acertos += 1
#         print(f'Acertou. Acertos: {acertos}')
#     else:
#         print(f'Errou. Acertos: {acertos}')

#     cont += 1

# print(acertos, 'acertos')

# matriz = [
#     [1,2,3],
#     [2,4,5],
#     [6,7,8],
#     [4,8,3]
# ]

# nao_repetidos = []
# repetidos = []

# for linha in range(0,4):
#     for coluna in range(0,3):
        
#         if matriz[linha][coluna] in nao_repetidos:
#             repetidos.append(matriz[linha][coluna])
   
#         nao_repetidos.append(matriz[linha][coluna])

# print(repetidos)

# matriz = [
#     ['o', 'x', ' '],
#     [' ', 'o', ' '],
#     ['x', ' ', 'o']
# ]

# for linha in range(0,3):
#     for coluna in range(0,3):
#         print(f'|{matriz[linha][coluna]}|', end=' ')
        
#     print('')
#     if linha != 2:
#      print('___________')

# alunos = [
#     ['', ''],
#     ['', ''],
#     ['', ''],
#     ['', ''],
#     ['', ''],
#     ['', ''],
#     ['', ''],
#     ['', ''],
#     ['', ''],
#     ['', '']
# ]

# for i ,linha in enumerate(range(0,10)):
#     for j, coluna in enumerate(range(0,2)):
#         alunos[linha][coluna] = float(input(f'Digite a nota {j+1} do aluno {i+1}: ')) #type: ignore
        


# for linha in range(0,10):
#     media = float((alunos[linha][0] + alunos[linha][1])) / 2
#     if media < 6:
#        print(f'aluno {linha+1} reprovado. MÉDIA: {media}')
#     else:
#        print(f'aluno {linha+1} aprovado. MÉDIA: {media}')

# matrizA = [
#     [2,5,4],
#     [4,5,2],
#     [6,9,2]
# ]

# matrizB = [
#     [1,9,12],
#     [5,11,2],
#     [4,5,2]
# ]

# matrizC = [
#     ['','',''],
#     ['','',''],
#     ['','','']
# ]

# for i, linha in enumerate(range(0,3)):
#     for j, col in enumerate(range(0,3,2)):
#         matrizC[linha][1] = matrizA[linha][1] + matrizB[linha][1]
#         matrizC[linha][col] = matrizA[linha][col] * matrizA[linha][col]


# for i, linha in enumerate(range(0,3)):
#     for j, col in enumerate(range(0,3)):
#         print(matrizC[linha][col], end=' ')
#     print()

# linhas = int(input('Numero de alunos: '))

# m = []
# for indice, i in enumerate(range(linhas)):
#     n = []
#     for indice2, j in enumerate(range(0,3)):
#         n.append(float(input(f'Aluno {indice+1}. Digite {indice2 + 1} a nota: ')))
#     m.append(n)

# for i, linha in enumerate(range(linhas)):
#     media = ((m[linha][0] * 3) + (m[linha][1] * 4) + (m[linha][2] * 3)) / 10
#     print(f'Aluno {i + 1}. Média: {media}')

# import numpy
# lin, col = 2,4

# matriz = numpy.zeros([lin,col])
# print(matriz)
        
# vetora = [1,2,3,5,5,6]
# vetorb = [1,2,3]

# for num in vetora:
#     vetorb.append(num)

# print(vetorb)


# lista = []

# for n in range(0,10):
#     lista.append(random.randint(1,1000))

# # print(len(lista))
# soma = 0
# for ele in lista:
#     print(ele)
#     soma = soma + ele
# print(soma/len(lista))

# vetora = []
# for rang in range(0,10):
#     vetora.append(random.randint(1,50))

# vetorb = []
# for i, num in enumerate(vetora):
#     if i % 2 == 0:
#         vetorb.append(num * 5)
#     else:
#         vetorb.append(num + 5)

# print(vetora)
# print(vetorb)

# vetora = []
# for rang in range(0,200):
#     vetora.append(random.randint(1,100))

# qtd = 0   
# for num in vetora:
#     if num % 4 == 0:
#         qtd +=1
#         print(num)

# print(qtd, 'números multiplos de 4')


# def escolheop(op, num1,num2):
#     if op == 1:
#         somar(num1,num2)
#     if op == 2:
#         subtrair(num1,num2)
#     if op == 3:
#         multiplicar(num1,num2)
#     if op == 4:
#         dividir(num1,num2)
#     if op == 5:
#         exponenciar(num1,num2)


# def somar(num1,num2):
#     print(num1 + num2)

# def subtrair(num1,num2):
#     print(num1 - num2)

# def multiplicar(num1,num2):
#     print(num1 * num2)

# def dividir(num1,num2):
#     print(num1 / num2)

# def exponenciar(num1,num2):
#     print(num1 ** num2)

# opcoes = [1,2,3,4,5]
# while True:
#     num1 = float(input('Digite o primeiro número: '))
#     num2 = float(input('Digite o segundo número: '))
#     print('Qual operação deseja realizar? 1 -> Somar; 2-> Subtrair; 3->Multiplicar; 4-> Divdir; 5-> Exponenciar. Digite "sair" para fechar.')
#     opc = int(input('Digite uma opção: '))
#     if opc not in opcoes:
#         print('Digite uma opção válida')
#         continue
#     escolheop(opc,num1,num2)
#     sair = input('deseja sair? ').lower()
#     if sair == 'sair':
#         break

# print('Adeus')


# m = []
# for indice, i in enumerate(range(0,1500)):
#     n = []
#     for indice2, j in enumerate(range(0,5)):
#         n.append(random.uniform(0,10))
#     m.append(n)

# menor5 = 0
# maior5 = 0
# for linha in range(0,1500):
#     for col in range(0,5):
#         if m[linha][col] < 5:
#             menor5 +=1
#         else:
#             maior5 +=1

# porcent1 = (menor5 * 100)/ 7500
# porcent2 = (maior5 * 100)/ 7500

# print(f'{round(porcent1,2)}% das notas foi menor que 5.')
# print(f'{round(porcent2,2)}% das notas foi maior que 5.')



# def existe(l,n):
#     achou = False
#     for i in range(len(l)):
#          if l[i] == n:
#              achou = True
#              break
#     return achou

# def maior(l):
#     m = l[0]
#     for i in range(len(l)):
#         if l[i] > m:
#             m = l[i]
#     return m

# v = []
# x = []
# for i in range(100):
#     v.append(int(random() * 1000) + )
#     x.append(int(random() * 500) + 1000)
    
# print (v)
# print (existe(v, 20))
# print ('O maior em v é', maior(v))
# print ('O maior em x é', maior(x))

# def fatorial (n):
#     r = 1
#     for i in range(1, n + 1):
#         r = r + 1
#     return r

# valor = int(input('Digite um número: '))
# result = fatorial(valor)
# print(f'Fatorial: {result}')



# from random import random

# velha = [['b','b','b'],
#          ['b','b','b'],
#          ['b','b','b']]
# fim = False
# ganhador = 'b'
# for li in range(3):
#     for co in range(3):
#         if fim == False:
#             if int(random() * 2) == 0:
#                 velha[li][co] = 'o'     
#             else:
#                 velha[li][co] = 'x'
#             print(velha[li][co], end='')
#     if fim == False:
#             if velha[0][0] != 'b' and velha[0][0] == velha[0][1] and velha[0][0] == \
#             velha[0][2]:
#                 fim = True
#             elif velha[1][0] != 'b' and velha[1][0] == velha[1][1] and velha[1][0] == \
#             velha[1][2]:
#                 fim = True
#             elif velha[0][0] != 'b' and velha[2][0] == velha[2][1] and velha[2][0] == \
#             velha[2][2]:
#                 fim = True
#             elif velha[1][0] != 'b' and velha[1][0] == velha[1][1] and velha[1][0] == \
#             velha[1][2]:
#                 fim = True
#             elif velha[1][0] != 'b' and velha[1][0] == velha[1][1] and velha[1][0] == \
#             velha[1][2]:
#                 fim = True
#             elif velha[1][0] != 'b' and velha[1][0] == velha[1][1] and velha[1][0] == \
#             velha[1][2]:
#                 fim = True
#             elif velha[1][0] != 'b' and velha[1][0] == velha[1][1] and velha[1][0] == \
#             velha[1][2]:
#                 fim = True
#             elif velha[1][0] != 'b' and velha[1][0] == velha[1][1] and velha[1][0] == \
#             velha[1][2]:
#                 fim = True
#     print()

import random

linhas = int(input('Numero de linhas: '))
colunas = int(input('Numero de colunas: ')) 

m = []
for i in range(linhas):
     n = []
     for j in range(colunas):
        # n.append(random.randint(0,50))  
        n.append(int(input('Digite um número: ')))
     m.append(n)

for lista in m:
    print(lista)
    print()
print('##############')

nova_matriz = []
for linha in range(colunas):
    novo = []
    for coluna in range(linhas):
        novo.append(m[coluna][linha])
    nova_matriz.append(novo)
        
for lista in nova_matriz:
    print(lista)
    print()
