#  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('='*17, '\n REAJUSTE DE 15%')
print('='*17)

sa = float(input('Insira o salário antigo do funcionário: R$'))
print('\nO salário reajustado com 15% de acrésimo resulta em R${:.2f}'.format(sa*1.15))
