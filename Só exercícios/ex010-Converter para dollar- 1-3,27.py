# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Cotação: 1- 3,27
from typing import Tuple

fc= 'CONVERSOR PARA DOLLAR'
print('='*30)
print(f'{fc:^30}')
print('='*30)

v = float(input('Digite o valor em reais: R$'))
d = v/3.27
print('Com essa quantia você pode adquirir US${:.2f}'.format(d))
