"""
def lambda, função anonima e uso para ordenação de listas
"""
l1 = [
    ['005', 548],
    ['075', 151],
    ['054', 454]
]

print(sorted(l1, key=lambda i: i[1], reverse=True))
print(sorted(l1, key = lambda item: item[1]))

def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)