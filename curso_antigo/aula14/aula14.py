
num1 = input('digite um númeuro: ')
num2 = input('digite um númeuro: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)

else:
    print('ERROR')