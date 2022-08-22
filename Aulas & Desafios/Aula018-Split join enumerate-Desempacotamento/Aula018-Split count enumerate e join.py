"""
Split- Dividi uma string
Join- Juntar uma lista
Enumerate- Enumerar elementos da lista
"""

string = 'O Brasil é o pais do futebol, o Brasil é penta'
l1 = string.split(' ')
l2 = string.split(',')

contagem = 0

for valor in l1:
    qtd = l1.count(valor)
    if qtd > contagem:
        palavra = ''
        contagem = qtd
        palavra += valor

print(f'A palavra que mais apareceu foi {palavra} {contagem}x')


a = '..'.join(l1)
print(a)

for indici, i in enumerate(l1):
    print(indici, i)

l3 = [
    [0,'O'],
    [1,'A'],
]

for f, h in l3:
    print(f, h)