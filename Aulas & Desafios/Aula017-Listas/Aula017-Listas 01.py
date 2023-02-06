"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
----------------------------------------------------
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# Listas são iteráveis, ou seja, tem índices

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
l3 = l1 + l2  # Cocatenação
l4 = list(range (0,11))
print(l3)
print((l4))
l1.extend(l2)  # Junta duas listas
print(l1)
print(max(l1), min(l1))
l1.extend('Oiiii') # Roda com hard code but separa cada caracter
print(l1)
l1.pop()  # Deleta um elemento, por padrão o ultimo
print(l1)
l1.pop(0)  # Testando a indexação dele
print(l1)
l1.append('Oii') # Junta a string inteira, porém no final
print(l1)
l1.insert(0, 'Banana') # Junta a string inteira onde eu quiser
print(l1)
l1.insert(-1, 'Meu povo') # Funciona negativo
print(l1)
del(l1[-1:-2])  # Apaga um elemento, mas não funciona negativo
del(l1[1:2])
l1.clear()
print(l1)
