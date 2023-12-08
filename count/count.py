
from itertools import count

contador = count(start = 9, step = -1)

for valor in contador:
    print(valor)
    if valor >= 10 or valor <= -10:
        break

