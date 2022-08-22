"""
Funções do proprío python e a importância da documentação
"""

a = input('digite um número: ')
d = a.isnumeric()
if d:
    a = int(a)
else:
    print(f'{a} não é númerico')

try:
    a = int(a)
    print(f'{a} é numerico')

except:
    print(f'{a} realmente não é numérico')
