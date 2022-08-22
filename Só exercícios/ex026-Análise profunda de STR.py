#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print("""
    =========================
    |Análise profunda de STR| 
    =========================\n\n""")

f = str(input('Digite a frase: ')).strip().upper()
print('A aparace {}X\nAparece pela primeira vez na posição {}\nAparece pela última vez na posição {}'.format(f.count('A'), f.find('A'), (f.rfind('A')+1)))

