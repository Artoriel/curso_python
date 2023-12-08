# for in
# função range(start = 0, stop, step = 1)

for n in range(0, 100, 8):
    print(n)


nome = 'phyton'
nova_string = ''

for letra in nome:
    if letra == 't':
        nova_string = nova_string + letra.upper()
        break
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra


print(nova_string)




