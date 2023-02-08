"""
While-laço de repetição
break- Acaba o laço geral
continue- pula aquele laço
"""
a = 0

while a != 6:
    if a == 4:
        a += 1
        continue
    print(a)
    a += 1
