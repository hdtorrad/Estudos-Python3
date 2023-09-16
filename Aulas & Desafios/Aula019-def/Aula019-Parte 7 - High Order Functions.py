"""
High Order Functions
Funções de primeira classe
tratadas como um tipo normal
"""

def saudacao(msg):
    return msg

def executa(funcao, texto):
    return funcao(texto)

print(executa(saudacao, 'Olá mundo!'))