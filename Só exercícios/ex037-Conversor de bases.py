"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
print("""
--=--=--=--=--=--=--=--=--
    Conversor de Bases
--=--=--=--=--=--=--=--=--

[B]ínario
[O]ctal
[H]exadecimal
""")

op = input('Digite a opção da base:').strip().upper()

if op != 'B' and 'O' and 'H':
    print('\033[1:31m Digite uma opção válido!!\033[m')
    op = input('Digite a opção da base:')

n = input('Agora, insira o número a ser convertido: ')
try:
    n = int(n)
except:
    print('\033[1:31m Digite um número!!\033[m')
    n = input('Agora, insira o número a ser convertido: ')

nc = ''
try:
    n = int(n)
    if op == 'B':
        while n > 0:
            nc = nc + str(n % 2)
            n = n // 2

        c = len(nc)
        ncc = ''

        while c > 0:
            c = c - 1
            ncc += nc[c]

        print(ncc)

    elif op == 'O':
        while n > 0:
            nc = nc + str(n % 8)
            n = n // 8

        c = len(nc)
        ncc = ''

        while c > 0:
            c = c - 1
            ncc += nc[c]

        print(ncc)

    elif op == 'H':
        print(f'{hex(n)[2:]}')
except:
    print('\033[1:31mDigite un número válido!!')
