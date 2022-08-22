# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

a = input('Digite o ano: ')
if a == 'atual':
    a = date.today().year

try:
    a = int(a)
    if a % 4 ==0 and a % 100 != 0 or a % 4 == 0 and a % 100 == 0 and a % 400 == 0:
        print(f'\033[35m{a} é bissexto!')
    else:
        print(f'{a} não é bisexto!')
except:
    print('\033[31mERROR!')