"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('-=-' * 8, ' CONVERSOR DE RELÓGIOS', '-=-' *8, sep = '\n')

horario= input('\nDigite o horário no relógio militar: ')

try:
    horario = int(horario)
    horario_americano = horario - 12 # Não existe horas negativas, por isso esta variavel não é usada em todas as opções

    if horario <= 24 and horario > 0:

        if horario >=0 and horario <= 11:
            print(f'\nBom dia!☀\033[m\nHorário convertido:', f'0{horario}:00am') 
        
        elif horario >= 12 and horario <= 17:
            print(f'\nBoa Tarde!☀\033[m\nHorário convertido: {horario_americano}:00pm')
        
        elif horario >= 18 and horario <= 24:
            print(f'\nBoa Noite!🌑\033[m\nHorário convertido: {horario_americano}:00pm')
    
    else:
        print('\nO dia só tem 24h e não existe hora negativa!!')

except:
    print('ERROR - DIGITE SOMENTE NÚMEROS!!')