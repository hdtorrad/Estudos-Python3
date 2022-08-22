# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('=' * 30, '\nCálculo da quantidade de tinta')
print('=' * 30)

lp = float(input('Insira a largura da parede(EM METROS!): '))
ap = float(input('Insira a altura da parede(EM METROS!): '))
tn = (lp * ap) / 2
print('Nessa parede será nescessário {:.2f} litros de tinta'.format(tn))
