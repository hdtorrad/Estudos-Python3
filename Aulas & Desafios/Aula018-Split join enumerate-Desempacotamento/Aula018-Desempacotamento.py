"""
Desempacotamento de listas:
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n1, n2, *resto_vira_lista = l
*lista, nu = l

print(l, n1, n2, resto_vira_lista, lista, nu, sep='\n\n')
