#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#  pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
#  por Km rodado.

print('='*19, '\n ALUGUEL DE CARROS')
print('='*19)


km = float(input('Insira a quantidade de km rodados: '))
d = int(input('Insira a quantidade de dias que o carro pernoitou com o cliente: '))
v = float((km * 0.15) + (d * 60))
print('\nO valor total do aluguel desse carro é R${:.2f}'.format(v))
