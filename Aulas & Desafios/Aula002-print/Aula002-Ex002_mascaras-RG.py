#  Criar máscara para RG, com print


RG = str(input('Insira seu RG(s/espaços): ')).strip()

print(f'{RG[:2]}.{RG[2:5]}.{RG[5:8]}-{RG[8:]}')

print('\nSeu RG já esta com máscara', end='!')
