"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""


def s1(*args):
    args = list(args)
    j = 0
    for i in args:
        args[j] = i + 1
        j += 1
    return args


def main(*args):
    args = list(args)
    f = 0
    j = 0
    for h in args:
        for i in args[j]:
            print(args[j][f])
            args[j][f] = f
            f += 1
        j += 1
    return args


a = list(main(s1(0, 2, 3, 85, 56, 351, 135, 351, 351, 123)))
print(*a, type(a))
