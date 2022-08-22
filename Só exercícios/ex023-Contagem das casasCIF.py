#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print("""
    =======================
      Separação das Casas   
    =======================\n\n""")

n = str(input('Insira o número: ')).strip()
a = len(n)
u = n[(a-1)]
d: int= n[(a-2):(a-1)]
c = n[(a-3):(a-2)]
m: int= n[(a-4):(a-3)]
if m == d:
    m = ''
print('Unidades: {}\nDezenas: {}\nCentenas: {}\nMilhar: {}'.format(u, d, c, m))
