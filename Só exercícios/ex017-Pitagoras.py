# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

from math import sqrt

print('=' * 20, '\nTEOREMA DE PITÁGORAS')
print('=' * 20)

co = float(input('Insira o cateto oposto: '))
ca = float(input('Insira o cateto adjacente:'))
h = (ca**2) + (co**2)
hr = sqrt(h)


print('Resultado: {:.2f}'.format(hr))



