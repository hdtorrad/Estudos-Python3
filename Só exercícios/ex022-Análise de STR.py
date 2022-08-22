""" Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome. """

print("""
    ===================
      Análise de STRs 
    ===================\n\n""")

n = input('Isira o nome a ser analisado: ')
n = n.strip()
ns = n.split(' ')

print('Análise Completa:\n{}- em maiúsculas\n{}-em minúsculas\n{}-tamanho do nome completo\n{}-tamanho do primeiro nome'.format(n.upper(), n.lower(), len(''.join(ns)), len(ns[0])))

