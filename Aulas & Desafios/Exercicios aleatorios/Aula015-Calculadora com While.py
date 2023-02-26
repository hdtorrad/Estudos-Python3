#Crie uma calculadora utilizando o loop while

flag = True

while flag:
    num1 = input("Insira o primeiro número: ")
    num2 = input("Insira o segundo número: ")

    try:
        num1 = int(num1)
        num2 = int(num2)
        
        operacao = input("Menu de Opções:\n[+] Adição\n[-] Subtração\n[*] Multiplicação\n[/] Divisão\n\nInsira a operação desejada: ").strip()
        
        if operacao == '+':
            print(f'{num1} somado a {num2} é {num1 + num2}')
        elif operacao == '-':
            print(f'{num1} subtraido a {num2} é {num1 - num2}')
        elif operacao == '*':
            print(f'{num1} multiplicado por {num2} é {num1 * num2}')
        elif operacao == '/':
            print(f'{num1} dividido por {num2} é {num1 / num2}')
        else:
            print("Digite uma operação válida")
    except:
        print("Insira somente números!!")

    continuar = input("Deseja continuar?\n[S]im ou [N]ão : ").lower()
    
    if continuar != 's':
        flag = False
    