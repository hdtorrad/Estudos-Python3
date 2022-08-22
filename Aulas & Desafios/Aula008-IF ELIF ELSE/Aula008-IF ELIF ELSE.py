"""
IF/ELIF/ELSE
"""

a = input('Você quer a verdade?\n').strip()

if a == 'sim':
    print('ok')
elif a == 'não sei':
    print('Ficar em cima do muro é uma opção')
else:
    print('A verdade tem um preço, que você tem que estar disposta a pagar...')
