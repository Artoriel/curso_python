numint = int(input('Digite um número para a taboada '))
cont = 0
while cont <= 10:
    res = cont * numint
    formatado = f'{numint} x {cont} = {res}'
    print(formatado)
    cont += 1




def bring_the_numbers(l1,l2):
    tamanho = min(len(l1), len(l2))
    exibe = [
            (l2[x],l1[x]) for x in range(tamanho)
        ]
    return exibe



num2 = input("Digite um valor para saber se é primo: ")
if num2.isdigit():
    num2int = int(num2)
    cont = 1
    qnt = 0
    lista_de_divisiveis = []
    listacont = ['primeiro','segundo','terceiro','quarto','quinto','sexto','setimo','oitavo',
                 'nono','decimo']
    while cont <= num2int:
        if num2int % cont == 0:
            qnt += 1
            lista_de_divisiveis.append(cont)    
            cont += 1
        else:
            cont += 1

    if qnt == 2:
        print(f'{num2int} é primo, e seus divisores são: ', end='\n')
        print(bring_the_numbers(lista_de_divisiveis,listacont))
    else:
        print(f'{num2int} não é primo, e seus divisores são: ', end='\n')
        print(bring_the_numbers(lista_de_divisiveis,listacont))
else:
    print("Valor inválido")