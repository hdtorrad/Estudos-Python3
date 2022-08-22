# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint

c = randint(1, 3)

if c == 1:
    c1 = 'Pedra'
elif c == 2:
    c1 = 'Papel'
elif c == 3:
    c1 = 'Tesoura'
else:
    print('\033[1:31mERROR_033')

print('''
\033[1:35m-=-=-=-=-=-=-=-=-=-\033[1:36m
      Jokenpô
\033[1:35m-=-=-=-=-=-=-=-=-=-\033[1:30m

Escolha sua opção:

[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura\033[m''')

u = input('')
try:
    u = int(u)
    if u == 1:
        u1 = 'Pedra'
    elif u == 2:
        u1 = 'Papel'
    elif u == 3:
        u1 = 'Tesoura'
    else:
        print('\033[1:31mERROR_DIGITE UMA DAS OPÇÕES')

    if u == c:
        print(f'\033[1:32mPC: {c1}\n\033[1:32mYOU: {u1}\n\033[1:33mEMPATE!🤪')
    elif u == 1:
        if c == 2:
            print(f'\033[1:32mPC: {c1}\n\033[1:32mYOU: {u1}\n\033[1:33mPC GANHOU!😪')
        else:
            print(f'\033[1:32mPC: {c1}\n\033[1:32mYOU: {u1}\n\033[1:33mYOU WIN!😉')
    elif u == 2:
        if c == 1:
            print(f'\033[1:32mPC: {c1}\n\033[1:32mYOU: {u1}\n\033[1:33mYOU WIN!😉')
        else:
            print(f'\033[1:32mPC: {c1}\n\033[1:32mYOU: {u1}\n\033[1:33mPC GANHOU!😪')
    elif u == 3:
        if c == 1:
            print(f'\033[1:32mPC: {c1}\n\033[1:32mYOU: {u1}\n\033[1:33mPC GANHOU!😪')
        else:
            print(f'\033[1:32mPC: {c1}\n\033[1:32mYOU: {u1}\n\033[1:33mYOU WIN!😉')
except:
    print('\033[1:31mERROR_OPÇÃO_INVÁLIDA!')
