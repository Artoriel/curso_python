'''''''''
desempacotando listas
'''''''''

'''lista = ['luiz', 'joao', 'artur', 1,2,3,4,5,6,7,8,9,10]

*outra_lista, n1, n2, n3 = lista

print(n1,n2,n3)
'''

lista = []
possiveis = ['i', 'a', 'l']
while True:
    print("Selecione uma opção: \n [i] -> inserir [a] -> apagar [l] -> listar ")
    opcao = input("Digite uma opção: ")
        
    if opcao in possiveis:
            if opcao == 'i':
                algo = input("Coloque o que deseja:")
                lista.append(algo)
            if opcao == 'a' and len(lista) == 0:
                print('lista vazia')
            if opcao == 'a' and len(lista) >=1:
                lista.pop()
            if opcao == 'l':
                print(lista)

        
    else:
        print("Você não digitou uma das opções")