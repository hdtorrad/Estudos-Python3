# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan, radians

print('='*26, '\n SENO, COSENO E TANGENTE')
print('='*26)

a = float(input('Insira o número para descobrir o seno, conseno e tangente: '))
n = radians(a)
print('Radianos: {:.2f}\nSeno: {:.2f}\nCoseno: {:.2f}\nTagente: {:.2f}'.format(n, sin(n), cos(n), tan(n)))