from datetime import datetime

data = datetime.strptime('2023-11-6 12:52:30', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%Y'), data.year)
         #str               #inteiro