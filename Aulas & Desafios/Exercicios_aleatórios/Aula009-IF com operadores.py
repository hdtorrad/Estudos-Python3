#Alterar  a ordem de exibição de um número dependendo se ele foi maior ou menor que outro

num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")

if num1 > num2:
    print(f'{num1=} é maior que {num2=}')
elif num1 < num2:
    print(f'{num2=} é maior que {num1=}')
else:
    print(f"{num1=} é igual a {num2=}")
