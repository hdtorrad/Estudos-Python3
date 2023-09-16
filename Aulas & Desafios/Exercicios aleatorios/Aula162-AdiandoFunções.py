# Exercício - Adiando execução de funções -- não consegui resolver, eu pensei em yield não em closure
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y



def criar_funcao(funcao, x):
    def intermedia(y):
        return funcao(x,y)
    return intermedia 


soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(3))
    
multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(10))