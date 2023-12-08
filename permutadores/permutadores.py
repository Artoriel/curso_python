
from itertools import combinations, product, permutations

pessoas = ['André', 'Luiz', 'Arthur', 'Axl']

for grupo in combinations(pessoas, 2):
    print(grupo)


