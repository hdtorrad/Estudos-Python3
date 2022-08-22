# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

fc = 'Tabuada'
print(f'{fc:=^20}')

n = int(input('\nInsira o número: '))
print(f'_'*15)
print('| {} X 00 = {:2} |\n| {} X 01 = {:2} |\n| {} X 02 = {:2} |\n| {} X 03 = {:2} |\n| {} X 04 = {:2} |\n| {} X 05 = {:2} |\n| {} X 06 = {:2} |\n| {} X 07 = {:2} |\n| {} X 08 = {:2} |\n| {} X 09 = {:2} |\n| {} X 10 = {:2} |'.format(n, n*0, n, n*1, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))
print('-'*15)
