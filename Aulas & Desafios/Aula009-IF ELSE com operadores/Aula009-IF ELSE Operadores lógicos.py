"""
== Igual
>= Igual ou maior que
<= Igual ou menor que
!= diferente
"""

n = int(input('Insira um número:\n'))
p = n % 2
if p != 0:
    print('{} é impar'.format(n))
else:
    print('{} é par'.format(n))