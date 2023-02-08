"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

CPF = input("Digite o CPF a ser validado: ").strip()

CPF = CPF.replace(".", '').replace('-',"")  #Para caso o usuário tenha inserido o CPF com os separadores

soma_2dig = 0
fator = 11

# Os dígitos que serão calculados são retirados da iteração
for numero in CPF[:10]: 
    soma_2dig += (int(numero) * fator)
    fator -= 1

dig2 = (soma_2dig * 10) % 11 

dig2 = dig2 if dig2 < 10 else 0     # Adequação ao requisito do dígito do CPF

print(soma_2dig, dig2)