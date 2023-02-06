'''
:s - Texto(str-strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(Número)f - QUantidade de casas decimais
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

ni = 2
nf = 2.0222
sa = 'oI'

print(f'{ni:0>2}')
print(f'{nf:.0f}')
print(f'{sa:#^20}')

su = sa.upper()
sl = sa.lower()
sc = sa.capitalize()
st = sa.title()

print(su)
print(sl)
print(sc)
print(st)

#Dá para usar a formatação de Strings como em C e em Java, usando o método de interpolação %
print("%s" % 'Exemplo')
print("%s %.2f %s %d" % ('Funciona float,', 1.23, 'int', 54))