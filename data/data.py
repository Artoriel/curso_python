from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

#strptime(str, fmt)
#.strftime(fmt)
#timestamp
#fromtimestamp()

data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=5)
print(data.strftime('%d/%m/%Y %H:%M:%S'))


setlocale(LC_ALL, '')
setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
ultimo_dia_mes = mdays[mes_atual]

# sábado, 13 de julho de 2019
formatacao1 = dt.strftime('%A, %d de %B de %Y')
# 13/07/2019 11:21:20
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1, formatacao2)
print(mes_atual, mdays[mes_atual])
