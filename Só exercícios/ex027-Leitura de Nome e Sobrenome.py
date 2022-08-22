# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.

print("""
    =========================
    |    Nome e Sobrenome   | 
    =========================\n\n""")

n = str(input('Digite seu nome: ')).strip().upper().split()

print('Nome: {}\nSobrenome: {}'.format(n[0].title(), n[len(n)-1].title()))
