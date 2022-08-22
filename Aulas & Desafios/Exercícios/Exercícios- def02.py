"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre
eles.
"""


def soma(n1=0, n2=0, n3=0):
    s = n1 + n2 + n3
    return s


num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))
num3 = float(input("Insira outro número: "))
r = soma(num1, num2, num3)
print(r)
