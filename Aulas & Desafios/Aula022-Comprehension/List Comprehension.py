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


lista = [1, 2, 3, 4, 5, 6, 7]

lista_quadrado = [i**2 for i in lista]

print(lista_quadrado)

# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)

# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# # print(novos_produtos)
# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
p(novos_produtos)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)