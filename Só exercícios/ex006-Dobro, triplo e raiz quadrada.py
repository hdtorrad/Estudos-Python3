# Crie um programa que calcule o dobro, triplo e a raiz quadrada de um número informado pelo usuário

fc = 'DOBRO>>TRIPLO>>RAIZ2'
print('{:=^50}'.format(fc))

n = int(input('Insira o número: '))
print('O número escolhido foi {}, logo:\nDobro:{}\nTriplo:{}\nRaiz quadrada:{:.2f}'.format(n, n*2, n*3, n**(1/2)))
