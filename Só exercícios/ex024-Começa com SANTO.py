# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

print("""
    ====================
    | COMEÇA COM SANTO | 
    ====================\n\n""")

c = str(input('Inisira sua cidade natal: ')).strip().upper().split()
print("SANTO" in c[0])