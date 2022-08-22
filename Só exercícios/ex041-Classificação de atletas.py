#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#  e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
aa = date.today().year
anatle = int(input('Insira o ano de nascimento do atleta: '))
id = aa - anatle
print(f'O atleta tem {id} anos logo,')

if id <= 9:
    print('É \033[1:35mMIRIM')
elif id <=14:
    print('É \033[1:35mINFANTIL')
elif id <= 19:
    print('É \033[1:35mJÚNIOR')
elif id <=25:
    print('É \033[1:35mSÊNIOR')
else:
    print('É \033[1:35mMASTER')