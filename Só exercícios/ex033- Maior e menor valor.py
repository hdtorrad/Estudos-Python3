# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
n3 = input('Digite o terceiro número: ')

try:
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)

    if n1 > n2 and n1 > n3:

        if n3 < n2:
            print(f'Maior: {n1:.2f}\nMenor: {n3:.2f}')
        elif n2 < n3:
            print(f'Maior: {n1:.2f}\nMenor: {n2:.2f}')
        else:
            print('\033[1:31mError!')

    elif n2 > n1 and n2 > n3:

        if n3 < n1:
            print(f'Maior: {n2:.2f}\nMenor: {n3:.2f}')
        elif n1 < n3:
            print(f'Maior: {n2:.2f}\nMenor: {n1:.2f}')
        else:
            print('\033[1:31mError!')

    elif n3 > n1 and n3 > n2:

        if n1 < n2:
            print(f'Maior: {n3:.2f}\nMenor: {n1:.2f}')
        elif n2 < n1:
            print(f'Maior: {n3:.2f}\nMenor: {n2:.2f}')
        else:
            print('\033[1:31mError!')

    else:
        print('\033[1:31mError!')

except:
    print('\033[1:31mError!')
