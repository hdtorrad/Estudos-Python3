"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""


def bsg(n):
    if not n % 3 and not n % 5:
        return 'BuzzFizz'
    elif not n % 3:
        return 'fizz'
    elif not n % 5:
        return 'buzz'
    else:
        return n


a = int(input('Digite um número: '))
e = bsg(a)
print(e)
