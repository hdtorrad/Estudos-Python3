"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""


def oi(saudacao='Oie,', nome='S/N'):
    print(saudacao, nome)


s = input('Digite uma saudação: ')
n = input('Digite um nome: ')

oi(s, n)
