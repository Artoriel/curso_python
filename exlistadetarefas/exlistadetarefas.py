
lista = ['jogar', 'estudar']


while True:
    opcao = int(input('Qual opção vc quer? '))

    if opcao == 1:
        lista.pop()
        print(lista)

    elif opcao == 2:
        print(lista)

    elif opcao == 3:
        tarefa = input('Adcione uma tarefa a sua lista: ')
        lista.append(tarefa)
        print(lista)
