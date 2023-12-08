
def sudacao(msg="Olá", nome="Artur"):
    print(msg,nome)


print(sudacao())

def soma(n1,n2,n3):
    print(n1+n2+n3)

somar = soma(100,200,300)
print(somar)

def aumento(n1,n2):
    n2 = (n2 + 100) / 100
    return n1 * n2

porcento = aumento(10, 10)
print(porcento)

def fizzbuzz(numero):
    if numero%3 == 0 and numero%5 == 0:
        return "fizzbuzz"
    elif numero%5 == 0:
        return 'buzz'
    elif numero%3 == 0:
        return "fizz"
    else:
        return numero
bus = fizzbuzz(9)
print(bus)