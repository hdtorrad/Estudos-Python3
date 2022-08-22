"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""
b = 0

def not_main():
    global b
    b = 1
    return 'deu certo'


def main(b):
    print(b)
    return b()


i = main(not_main)
print(b, i)
