# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('='*8, '\nDESCONTO')
print('='*8)

pa = float(input('Digite o preço antigo: R$'))
print('O preço desse produto com 5% resulta em R${:.2f}'.format(pa * 0.95))
