# C:\diretorio
import os
# caminho = r'C:\\diretorio'
caminho = os.path.join('C:\diretorio')
print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue
    
    for item in os.listdir(caminho_completo_pasta):
        print('   ', item)