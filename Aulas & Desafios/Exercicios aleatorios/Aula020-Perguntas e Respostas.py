# Exercício - sistema de perguntas e respostas
import os

pergunta = [
    {
        'Pergunta': 'Quem ganhou o carnaval 2023?',
        'Alternativas': ['Mocidade', 'Independente', 'Rosas', 'Vila Maria', 'Vai-Vai'],
        'Resposta': 'Mocidade'    
    },
    
    {
        'Pergunta': 'Qual é o meu cantor(a) favorito(a)?',
        'Alternativas': ['Mitski', 'BB rexha', 'Ricky Montegomery', 'Alen Faded', 'Não tenho um cantor(a) favorito(a)'],
        'Resposta': 'Mitski'    
    },
    
    {
        'Pergunta': 'Qual minha linguagem de programação favorita?',
        'Alternativas': ['Python', 'Java', 'C', 'C#', 'Java-Script'],
        'Resposta': 'Java'    
    }
]

fator_alternativas = 97
acertos = 0
numero_pergunta = 0

while numero_pergunta < len(pergunta):
    print(pergunta[numero_pergunta]['Pergunta'])
    
    for alternativa in pergunta[numero_pergunta]['Alternativas']:
        print(f'{chr(fator_alternativas)}-) {alternativa}', end ='\t')
        fator_alternativas += 1
    
    print('\n')
    resposta = input("Insira a alternativa correta: ")
    resposta = pergunta[numero_pergunta]['Alternativas'][ord(resposta) - 97]
    
    if pergunta[numero_pergunta]['Resposta'] == resposta:
        print("\n\nVOCÊ ACERTOU! 😁")
        acertos += 1
    else:
        print("\n\nVOCÊ ERROU! 😢\n\n")
    
    input('Pressione qualque tecla para continuar:/')
    os.system('cls')
    
    numero_pergunta += 1
    fator_alternativas = 97
    
print(f'VOCÊ ACERTOU {acertos} de {len(pergunta)}')
    