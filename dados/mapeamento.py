from dados import pessoas, produtos, lista
from functools import reduce


def aumentapreco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novas_produtos = map(aumentapreco, produtos)

for produto in novas_produtos:
    print(produto)


nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))


soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idades / len(pessoas))