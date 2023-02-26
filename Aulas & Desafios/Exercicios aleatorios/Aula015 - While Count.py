# Contar as letras que mais aparecem em uma frase

frase = input("Insira a frase a ser contada as letras:")

i = 0
mais_comum = 0
letra_mais_comum = ''

while i < len(frase):
    if mais_comum < frase.count(frase[i]):
        mais_comum = frase.count(frase[i])
        letra_mais_comum = frase[i]
    i = i + 1

print(f"A letra que mais apreceu foi {letra_mais_comum}")