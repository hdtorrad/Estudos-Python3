# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

s1 = input('Digite o primeiro segmento do triângulo: ')
s2 = input('Digite o segundo segmento do triângulo: ')
s3 = input('Digite o terceiro segmento do triângulo: ')

try:

    s1 = float(s1)
    s2 = float(s2)
    s3 = float(s3)

    if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
        print('Forma um triângulo!')
        if s1 == s2 == s3:
            print('Este triângulo é equilátero')
        elif s1 == s2 or s1 == s3 or s2 == s3:
            print('Este triângulo é isósceles')
        else:
            print('Este triângulo é escaleno')
    else:
        print('Não forma um triângulo!')

except:
    print('\033[1:31mInforme somente números')
