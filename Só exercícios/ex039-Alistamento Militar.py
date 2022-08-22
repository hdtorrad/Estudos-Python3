# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
# se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date

aa = date.today().year

aj = int(input('Digite o seu ano de nascimento: '))
ij = aa - aj

if ij < 18:
    print(f'Você ainda não tem que se alistar, porém em {18-ij} anos terá...')
elif ij == 18:
    print('Você deve se alistar esse ano!')
else:
    print(f'You supposted to be alisted at {ij-18} years ago')