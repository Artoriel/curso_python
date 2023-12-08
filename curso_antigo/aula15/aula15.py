# pass e ellipsis(...)



'''
    valor = False

if valor:
    ...
else:
    print('bye.')
'''

'''
cont = 0
qntd = 0
menor = 0
maior = 0 

while cont <= 3:
    
    num = int(input("Digite um número: "))
    qntd += 1
    
    if qntd == 1:
        maior = menor = num
        cont += 1
    else:
        if num > maior:
            maior = num
            cont += 1
        elif num < menor:
            menor = num
            cont += 1     
        else:
            cont += 1
    
print(f'a diferença do maior "{maior}" e menor "{menor}" é {maior - menor}')   
'''


num = input("Digite um número: ")
num = int(num)
cont = 1 
divisores = 0
while cont <= num:
    if num % cont == 0:
        divisores += 1
        cont+=1
    if num % cont != 0:
        cont +=1



if divisores == 2:
    print("primo")

else:
    print("nao primo")

    
pu = float(input('Digite o preço unitário do produto: R$'))
qt = int(input('Digite a quantidade vendida do produto: '))
venda = pu * qt
desc = float(input('Digite o valor do desconto em reais: R$'))
total = venda - desc
if desc > venda:
   print('O desconto é maior que o valor da venda')
else:
   print('====================================================================')
   print(f'O valor bruto é de R${venda:,.2f} e seu desconto é de R${desc:,.2f}')
   print(f'O valor total da compra foi de R${total:,.2f}')  


    
     


