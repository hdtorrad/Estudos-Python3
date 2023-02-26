# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def duplica(num):
    def quadriplica(result_preview):
            return f'{result_preview}, {num * 4}'
    def triplica(result_preview):
            return quadriplica(f'{result_preview}, {num * 3}')
    return triplica(f'{num * 2}')

print(duplica(2))