#  Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# ºC x 1,8 + 32

print('='*28, '\n CONVERSOR DE TEMPERATURA')
print('='*28)

c = float(input('Insira a temperatura em ºC: '))
f = c * 1.8 + 32
print('{:.2f}ºC equivale a {:.2f}ºF'.format(c, f))

