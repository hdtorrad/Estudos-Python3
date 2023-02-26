# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*args):
    total = 1 # Porque x * 0 = 0
    for numero in args:
        total *= numero
    return total

argumentos = []
while True:
    argumento = input("Insira os numeros a serem multiplicados (Insira qualquer letra para interromper a leitura): ")
    if argumento.isdigit():
        argumentos.append(int(argumento))
    else:
        break

resultado = multiplicacao(*argumentos)
print(f"O resultado foi: {resultado:,.2f}")

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if not numero % 2:
        return "par!"
    else:
        return "impar!"

numero = int(input("Insira um número para saber se ele é impar ou par: "))
resultado = par_impar(numero)
print(f"{numero} é {resultado}")