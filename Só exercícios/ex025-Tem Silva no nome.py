# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print("""
    ====================
    |   TEM SILVA!!!!! | 
    ====================\n\n""")

n = str(input('Insira seu nome: ')).strip().upper()
print('SILVA' in n)

