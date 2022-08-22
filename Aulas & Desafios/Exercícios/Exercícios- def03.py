"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


def aumento(v, a):
    result = (v * (a/100)) + v
    return result


valor = float(input("Digite o valor: "))
acre = float(input('Digite o acrésimo: '))
r = aumento(valor, acre)
print(r)
