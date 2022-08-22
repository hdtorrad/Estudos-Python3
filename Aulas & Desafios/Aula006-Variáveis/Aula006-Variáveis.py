"""
letras minúsculas, sem números no começo, nomes compostos juntos por_, menor nome possível
"""
nome = 'Humberto da Torre Murad'
idade = 16
altura = 1.69
peso = 102
maioridade = idade >= 18
imc = peso/altura ** 2

print('''
Nome = {}
Idade = {}
Altura = {}
Peso = {}
Possui maioridade penal. ({})
IMC= {:.2f}'''.format(nome, idade, altura, peso, maioridade, imc))
