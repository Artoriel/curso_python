''''''''''
funções def
'''''''''''

def saudacao( msg='oi', nome="Artur"):
    return f"{msg}, {nome}"

def divide(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

divisao = divide(10,0)
variavel = saudacao()

print(variavel)
print(divisao)