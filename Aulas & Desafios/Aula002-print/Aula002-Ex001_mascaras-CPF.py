#  Crie um programa que coloca os números dos documentos em suas máscaras

CPF = str(input('Insira seu CPF(s/espaços): ')).strip()
print(f'{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}', 'CPF arrumado!', sep = '\n')
