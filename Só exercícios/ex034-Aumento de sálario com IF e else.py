# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.

sa = input('Insira o salário anterior: ')

sa = float(sa)

if sa <= 1250.00:
    sa = sa * 1.15
    print(f'\033[36mSeu salário agora é R${sa:.2f}')
else:
    sa = sa * 1.10
    print(f'\033[36mSeu salário agora é R${sa:.2f}')
