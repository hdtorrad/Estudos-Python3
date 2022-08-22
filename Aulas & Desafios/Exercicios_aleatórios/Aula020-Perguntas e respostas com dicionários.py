"""
Criar um sistema de perguntas e respostas!
"""
from typing import Tuple, Dict

dic = {
    "Pergunta 1": {
        "pergunta": 'Estou gostando do curso?',
        'respostas': {'a': 'Sim claro!', 'b': 'Óbvio, Otavio Mirando perfeito nunca errou', 'c': 'Não'},
        'respc': 'a'},
    "Pergunta 2": {
        "pergunta": 'Você está surtando?',
        'respostas': {'a': 'Sim claro!', 'b': 'Não'},
        'respc': 'a'},
    "Pergunta 3": {
        "pergunta": 'Você está cansado de python?',
        'respostas': {'a': 'Sim!', 'b': 'Não sei', 'c': 'Não!'},
        'respc': 'c'},
    "Pergunta 4": {
        "pergunta": 'Quero ir para o curso de SI?',
        'respostas': {'a': 'Obvío', 'b': 'Não o outro curso é pior', 'c': 'Não, quero terminar Python!'},
        'respc': 'c'}

}

for key, valor in dic.items():
    print(f'{key}:\n{valor["pergunta"]}\n\nAlternativas:')
    for alternativa, resp in valor["respostas"].items():
        print(f'[{alternativa}] - {resp}')
    print()
    resposta_usuario = input('Digite a opção certa:\n')
    print('CORRETO!!!' if resposta_usuario == valor['respc'] else 'Errou')
