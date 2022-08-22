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
