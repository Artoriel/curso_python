
    if num % cont == 0:
        divisores += 1
        cont+=1
    if num % cont != 0:
        cont +=1



if divisores == 2:
    print("primo")

else: