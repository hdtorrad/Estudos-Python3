"""
Len- só funciona com str
"""
a = input('Digite seu usuário: ')
b = len(a)

print(a, b, type(b), a.__len__(),  sep='\n')
