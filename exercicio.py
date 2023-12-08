import copy, pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

def ordena(lista, valor):
    try:
        if isinstance(valor, str):
            return sorted(lista, key=lambda item: item[valor])
    except KeyError:  
        return f'{valor} é inválido.'

def copia_profunda(lista):
    return copy.deepcopy(lista)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = copia_profunda(produtos)
novos_produtos = [
    {**produto, 'preco':round(produto['preco'] * 1.1, 2)}
    for produto in produtos
]
p(novos_produtos)
print()
# produtos_ordenados_por_nome = copia_profunda(produtos)
# produtos_ordenados_por_nome = ordena(produtos, 'nome')
# p(produtos_ordenados_por_nome)

print()
# produtos_ordenados_por_preco = copia_profunda(produtos)
# produtos_ordenados_por_preco = ordena(produtos, 'preco')
# p(produtos_ordenados_por_preco)

print()

p(produtos)
while True:
    atributo = input('Qual a atributo você quer ordernar? ').lower()
    p(ordena(produtos, atributo))


# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)