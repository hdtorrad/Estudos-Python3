"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
c = float(input('Insira o valor da casa: R$'))
s = float(input('Insira o seu redimento mesnsal: R$'))
a = int(input('Insira em quantos anos deseja pagar: '))

pm = c / (a * 12)
e = pm <= s * 0.3
print('Parabéns, emprestimo aprovado!' if e else 'Infelizmente seu emprestimo foi negado')
