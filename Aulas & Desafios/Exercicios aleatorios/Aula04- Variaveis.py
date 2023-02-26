# Criar variáveis

import datetime
data = datetime.date.today()

nome = "Humberto"
sobrenome = "Murad"
idade = 17
ano_nascimento = data.year - idade
maior_idade = idade >= 18
altura = 1.69

print("Nome: ", nome)
print("Sobrenome: ", sobrenome)
print("Idade: ", idade)
print("Ano de Nascimento: ", ano_nascimento)
print("É maior: ", maior_idade)
print("Altura em metros: ", altura)
