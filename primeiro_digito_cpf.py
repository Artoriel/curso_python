cpf = '74682489070'
cpf_9= cpf[:9] 
total = 0
contagem = 10


for num in cpf_9:
    
    resul = int(num) * contagem
    total += resul
    contagem -= 1

total = total * 10
total_resto = total % 11

if total_resto >= 10:
    total_resto = 0
else:
    total_resto = total_resto

total_resto = str(total_resto)

cpf_primeiro_digito = cpf[:9]  + total_resto



cpf_10 = cpf_primeiro_digito[:10]


total2 = 0
contagem2= 11


for num in cpf_10:
    
    resul2 = int(num) * contagem2
    total2 += resul2
    contagem2 -= 1

total2 = total2 * 10
total_resto2 = total2 % 11

if total_resto2 >= 10:
    total_resto2 = 0
else:
    total_resto2 = total_resto2

total_resto2 = str(total_resto2)

novo_cpf = cpf[:9] + total_resto + total_resto2
print(novo_cpf)

if novo_cpf == cpf:
    print('Válido')
else:
    print("Inválido")












