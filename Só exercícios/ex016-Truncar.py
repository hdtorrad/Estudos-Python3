# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

print('=' * 9, '\n TRUNCAR')
print('=' * 9)

n = float(input('Digite um número para ser truncado: '))
print('\nO número truncado resulta em {}'.format(trunc(n)))
