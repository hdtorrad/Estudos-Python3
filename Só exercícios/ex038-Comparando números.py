'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

n1 = input('Insira um número: ')
n2 = input('Insira outro número: ')

try:
    n1 = int(n1)
    n2 = int(n2)
    if n1 == n2:
        print('\033[1:33mAmbos são iguais!')
    elif n1 > n2:
        print('\033[1:34mO primeiro valor é maior!')
    else:
        print('\033[1:35mO segundo número é o maior!')

except:
    print(f'\033[1:31m{n1} ou {n2} não é um número sua anta!')