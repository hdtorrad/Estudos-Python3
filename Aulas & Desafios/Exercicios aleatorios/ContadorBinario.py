"""
Exercício do CodeWars, que conta os 1 do número em binário!
"""

numero = int(input("Insira um número\n"))
binario = bin(numero)
qntde1 = 0
for i in range(len(binario)):
    if binario[i] == '1':
        qntde1 += 1
print(qntde1)
