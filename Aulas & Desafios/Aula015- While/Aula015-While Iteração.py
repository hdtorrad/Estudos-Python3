"""
Iteração consiste em passar algo em todos os coponentes de algo itinerável
Ex: Ordenação de vetores, upper só algumas letras e coisas do tipo
"""
a = 'All I want is nothing more, to hear you knocking at my door, cause if I could see you face once more'
i = 0
na = ''
while i != len(a):
    if a[i] == 't':
        na += 'T'
    else:
        na += a[i]
    i += 1

print(na)
