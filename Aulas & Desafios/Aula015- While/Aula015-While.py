"""
While-laço de repetição
break- Acaba o laço geral
continue- pula aquele laço
"""
a = True

while a:

    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    o = input('Informe o operador: ')

    try:
        n1 = float(n1)
        n2 = float(n2)
        if o == '+':
            print(f'Result: {n1 + n2}')
        elif o == '-':
            print(f'Result: {n1 - n2}')
        elif o == '*':
            print(f'Result: {n1 * n2}')
        elif o == '/':
            print(f'Result: {n1 / n2}')
        else:
            print('\033[1:31mDigite um operador válido!\033[m')

    except:

        print('\033[1:31mDigite somente números!!\nばか\033[m')

    while a != 'N' or 'S':
        a = input('\nDeseja encerar o programa? [N]ão [S]im \n')
        if a == 'N':
            a = True
            break
        elif a == 'S':
            a = False
            break
        else:
            print("Digite 'S' ou 'N'")



