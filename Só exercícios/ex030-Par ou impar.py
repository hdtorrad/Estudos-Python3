# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

a = input('\033[1:34mDigite um número:\n')

try:
    a = int(a)
    if 2 % a == 0:
        print(f'{a} é par!')
    else:
        print(f'{a} é ímpar!')
except:
    print('ERROR')