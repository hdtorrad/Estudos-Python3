# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

a = (input('Digite a velocidade do carro:\n'))
try:
    a = (80 - int(a)) * -1
    b = a * 7
    if a == 0:
        print('Velocidade dentro do limite!\nHave a good day!')
    else:
        print(f'Execedeu a velocidade máxima em {a}km/h', 'Logo terá de pagar uma multa de R${:.2f}'.format(b), sep='\n')
except:
    print('ERROR')