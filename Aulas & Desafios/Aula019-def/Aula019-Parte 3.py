"""
*Args **Kwargs
"""


def f(*args, **kwargs):
    for a in args:
        print(a)
    print(f'\033[1:31m {kwargs["n"]} \033[m')

def teste(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)
    for valor in args:
        print(valor)

finaltest= 'rolou?'

teste(1,2,3,4,5,6,7,8,9,10, finaltest, t= 'tudo', s = 'Se só funcionar nomeando na chamda é zuado')
lista = [1,2,3,4,5,6,7,8,9,10]
a = "oias"
f(*lista, 20, 50, a, n='Oi')

# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)