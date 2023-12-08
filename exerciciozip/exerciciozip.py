

lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4]

soma = zip(lista1, lista2)

for num1, num2 in soma:
    print(num1 + num2)