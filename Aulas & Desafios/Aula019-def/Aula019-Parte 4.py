"""
GLOBAL, pode-se passar funções pelo return b()
"""

a = 'é varialvél global pq esta no escopo global e no começo(eu acho)'


def globa():
    print(a)


b = ' mentira eu to errado'


def teste():
    global a, b
    a += b
    print(a)


def muda():
    global a, b

    a += 'Não é uma boa pratica isso'
    b += 'Não é uma boa pratica isso'
    print(a, b)


globa()
teste()
muda()