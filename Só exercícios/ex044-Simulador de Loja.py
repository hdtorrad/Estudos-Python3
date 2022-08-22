# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print('\033[1:36m-=-'*4, '\033[1:33m LOJAS GHTM', '\033[1:36m-=-\033[m'*4, sep='\n')

p = float(input('Digite o valor a ser pago: R$'))

print('''
\033[1:35m------------Forma de Pagmento------------\033[1:37m

A vista:
    [D]inheiro ou cheque
    [C]artão
A prazo:
    [2]x
    [3]x ou mais\n\033[m''')

op = input('Digite a forma de pagmento: ')

if op == 'D':
    p = p * 0.9
elif op == 'C':
    p = p * 0.95
elif op == '2':
    print(f'Serão 2 parcelas de R${p/2:.2f}')
elif op == '3':
    qp = int(input('Digite o número de parcelas: '))
    p = p * 1.2
    pc = p / qp
    print(f'Valor da parcela: R${pc:.2f}')
print(f'Valor total a ser pago: R${p:.2f}')