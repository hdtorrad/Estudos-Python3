"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n = input('Digite um número: ')

try:

    n = int(n)

    if n % 2 != 0:
        print(f'\033[1:36m{n}\033[m é ímpar!')
    else:
        print(f'\033[1:36m{n}\033[m é par!')

except:

    print(f'\033[1:31m{n} não é um número inteiro!!!!')