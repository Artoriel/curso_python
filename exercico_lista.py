
# def listar(lista=None):
#     if len(lista) == 0:
#         return 'lista vazia!'
#     for item in lista:
#         print(item)

# def desfazer(lista=None):
#     if len(tarefas) == 0:
#          return 'LISTA VAZIA!'
#     global aux
#     aux = lista.pop()      
    
# def refazer(lista):
#     lista.append(aux)


# tarefas = []
# comandos = ['LISTAR', 'DESFAZER', 'REFAZER']
# while True:
#     print('LISTA DE TAREFAS.', end= '\n')
#     print('\n')
#     print('COMANDOS: LISTAR, DESFAZER E REFAZER')
#     comando = input('Selecione um comando: ').upper()
    
#     if comando == 'LISTAR':
#         listar(tarefas)
#     if comando not in comandos:
#         tarefas.append(comando)
#         listar(tarefas)
#     if comando == 'DESFAZER':
#         desfazer(tarefas)
#         listar(tarefas)
#     if comando == 'REFAZER':
#         refazer(tarefas)
#         listar(tarefas)



import json
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando() #type: ignore
    salvar(tarefas, CAMINHO_ARQUIVO)