#  Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
#  Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
from datetime import date

n = input('Insira seu nome: ')
i = int(input('Insira sua idade: '))
a = float(input('Insira sua altura: '))
p = float(input('Insira seu peso: '))
aa = date.today().year

an = aa - i
imc = p / a ** 2

print(f'{n} tem {i} anos, {a}m e {p:.2f}kg, logo seu IMC é {imc:.2f}\nComo estamos em {aa}, {n} nasceu em {an}')

if imc < 18.5:
    print('Você está abaixo do peso: ')
elif imc <= 25:
    print('Você está com um peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print('Você está em um estado de obesidade')
elif imc > 40:
    print("Você está em um estado de obesidade mórbida")
