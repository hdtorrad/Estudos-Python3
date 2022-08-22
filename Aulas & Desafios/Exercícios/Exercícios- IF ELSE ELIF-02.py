"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('\033[1:35m-=-'*8, ' CONVERSOR DE RELÓGIOS', '\033[1:35m-=-\033[m'*8, sep = '\n')
tm = input('\nDigite o horário no relógio militar: ')

try:
    tm = int(tm)
    ta = tm - 12
    ta = int(ta)

    if tm < 24:
        if ta <= 0:
            if tm < 12:
                print(f'\n\n\033[1:33mBom dia!☀\033[m\nHorário convertido:', f'0{tm}:00am' if tm < 10 else f'{tm}:00am')
            else:
                print(f'\n\n\033[1:33mBoa Tarde!☀\033[m\nHorário convertido: 00:00pm')
        else:
            if tm <= 17:
                print(f'\n\n\033[1:33mBoa Tarde!☀\033[m\nHorário convertido: {ta}:00pm')
            else:
                print(f'\n\n\033[1:33mBoa Noite!🌑\033[m\nHorário convertido: {ta}:00pm')
    else:
        print('\n\n\033[1:31m24 no relógio mundial é igual a 00' if tm ==24 else '\033[1:31mO dia só tem 24h!!')

except:
    print('\033[1:31mERROR - DIGITE SOMENTE NÚMEROS!!')