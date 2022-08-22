"""
While-laço de repetição
Else- Q nem do IF
"""

a = int(input('Digite um número: '))
i = 0

while i <= 100:
    if i == a:
        print(f"{a} está entre 0 e 100")
        break

    else:
        i += 1
else:
    print(f'{a} não entá entre 0 e 100!')
