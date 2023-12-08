from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'exemplo.csv'
print(CAMINHO_CSV)

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)