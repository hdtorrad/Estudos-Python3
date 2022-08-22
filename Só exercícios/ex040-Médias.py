# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

mf = (n1 + n2) / 2

if mf < 5:
    print('\033[1:31mXIIII... Reprovou!')
elif mf >= 5 and mf < 7:
    print('\033[1:31mVocê está de recuperação!')
elif mf >= 7:
    print('\033[1:33mVocê esta aprovado! ')