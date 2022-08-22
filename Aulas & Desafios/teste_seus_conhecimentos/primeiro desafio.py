"""
*Criar variáveis para nome (str), idade (int),
*altura (float) e peso (float) de uma pessoa
*Criar uma variável com o ano atual(int)
*Obter o ano de nascimento da pessoa
*Obter o IMC da pessoa
*Exibir usando F-Strings
"""

n = 'Humberto da Torre Murad'
i = 17
a = 1.69
p = 102.00
aa = 2022
an = aa - i
imc = p / a ** 2

print(f'{n} tem {i} anos, {a}m e {p:.2f}kg, logo seu IMC é {imc:.2f}\nComo estamos em {aa}, {n} nasceu em {an}')
