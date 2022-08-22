# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

print('='*19, '\n LISTA EMBARALHADA')
print('='*19)

g1 = input('Insira o primeiro grupo: ')
g2 = input('Insira o segundo grupo: ')
g3 = input('Insira o terceiro grupo: ')
g4 = input('Insira o quarto grupo: ')

l = [g1, g2, g3, g4]
shuffle(l)

print('Ordem de apresentação dos trabalhos:\n{}'.format(l))
