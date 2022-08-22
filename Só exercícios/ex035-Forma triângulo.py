# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.

s1 = input('Digite o primeiro segmento do triângulo: ')
s2 = input('Digite o segundo segmento do triângulo: ')
s3 = input('Digite o terceiro segmento do triângulo: ')

try:

    s1 = float(s1)
    s2 = float(s2)
    s3 = float(s3)

    if s1 + s2 > s3:
        if s1 + s3 > s2 :
            if s2 + s3> s1:
                print('Forma um triângulo!')
    else:
        print('Não forma um triângulo!')

except:
    print('\033[1:31mInforme somente números')
