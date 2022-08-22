# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

print('='*23, '\n QUEM APAGARÁ A LOUSA❓')
print('='*23)

n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')

l = [n1, n2, n3, n4]

a = random.choice(l)
print('Pois eh...\nFoi tu:\n¯\_(ツ)_/¯ {} ¯\_(ツ)_/¯'.format(a))
