"""
Operação ternária com listas kkkkkk
"""

li = list(range(1, 101))
print(li)
l1 = [i for i in li if i % 2 == 0]
print(l1)

l2 = [i for i in li if not i % 2 == 0]
print(l2)

l3 = [i * 2 for i in li]
print(l3)

lstr = ['      Oi            ', '            Isso      ', 'é ', '     um', 'teste ']
l4 = [i.capitalize().replace('o', "O").strip() for i in lstr]
print(l4)

tupla = (('chave', "valor"), ('outra chave', 'outro valor'))
l5 = [(x,y) for x,y in tupla]
print(l5)


lista = [1, 2, 3, 4, 5 ,6 ,7]


lista_quadrado = [i**2 for i in lista]

print(lista_quadrado)

