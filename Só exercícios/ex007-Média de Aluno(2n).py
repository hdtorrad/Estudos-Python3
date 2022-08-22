# Crie um programa que leia duas notas de um aluno e apresente sua média:

fc= 'CALCULADORA DE MÉDIA'
print('{:=^50}'.format(fc))
n1 = float(input('Digite a primeria nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A média desse aluno é {:.2f}'.format(m))
