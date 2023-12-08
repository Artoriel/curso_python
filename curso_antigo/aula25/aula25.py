'''''''''
split, join e enumerate
'''''''''

string = 'O Brasil é o país do futebol, o Brasil é penta.'


lista_1 = string.split(' ')

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')

stringg = 'O Brasil é penta'
lista = stringg.split(' ')
string2 = ','.join(lista)
print('')
print(string2)



for indice, valor in enumerate(lista):
    print(indice, valor)
