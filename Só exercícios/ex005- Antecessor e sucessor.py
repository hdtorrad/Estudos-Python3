# Criar um programa que calcula o número sucessor e antecessor do número informado pelo usuário

fc = 'MOSTRAR O ANTECESSOR E O SUCESSOR DE UM NÚMERO'
print('{:=^56}'.format(fc))
n = int(input('Digite o número: '))
print('O antecessor do número informado é {}, o número informado foi {}, logo seu sucessor é {}'.format(n-1, n, n+1))
