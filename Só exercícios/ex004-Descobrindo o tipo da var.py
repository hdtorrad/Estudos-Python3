# Crie um programa que mostre o tipo da variável e todas as informações possíveis sobre ela.

var = input('Digete algo: ')

print('É do tipo', type(var))
# type mostra o tipo

print('É só número: ', var.isnumeric())
# var.isnumeric() é se é só número

print('É alfabético: ', var.isalpha())
# var.isalpha() é se é alfabético

print('É alfanumérico: ', var.isalnum())
# var.isalnum() é se é alfanumérico

print('São espaços: ', var.isspace())
# var.isspace() é se é espaço

print('É tudo maiúsculo: ', var.isupper())
# var.isupper() é se é tudo maiusculo

print('É tudo minúsculo: ', var.islower())
# var.islower() é se é tudo minúsculo

print('É capitalizada: ', var.istitle())
# var.istitle() é se é capitalizada, misturado A e a

