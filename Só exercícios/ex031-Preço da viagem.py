# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

a = input('Digite o tamanho da viagem: ')

try:
    a = int(a)
    if a > 200:
        a = a * 0.45
        print('Total: R${:.2f}'.format(a))
    else:
        a = a * 0.50
        print('Total: R${:.2f}'.format(a))
except:
    print('\033[31mERROR!')
