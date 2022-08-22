"""
Dicionários
"""

dic = {'chave': 'Valor da chave', 'outra chave': 'valor da outra chave'}
print(dic)
print(dic['chave'])
print(*dic)

for k in dic:
    print(k)
    print(k, dic[k])

a = input('Digite a chave:')
b = input('Digite o valor da chave:')

dic[a] = b
print(dic)

dic1 = dict(chave='valor da chave', outra_chave='valor da outra chave')  # Outro jeito de se criar dicts
print(dic1)

outro_dic = {
    'strs': 'Válido',
    123: 'Válido',
    (1, 2, 3, 4): 'Válido',
    1.23: 'Será q funciona?',
    True: 'Ultimo teste'
}

sla = ("a", 12, 1.23, True)
print(f'(sla)')
print(f'{outro_dic}')

dic.update({'sla': "sla"})

if dic.get('sla') is not None:
    print(dic['sla'])

del dic['sla']  # Ou dic.pop(NOME DA CHAVE A SER APAGADA!)

if dic.get('sla') is not None:
    print(dic['sla'])

# dic.items(), checa os pares
# dic.values(), checa os valores
# dic.keys, intuitivo né?
# len em dict mede os pares
# Dicts aceitam cocatenação
v = dic  # Gera uma relação entre os dicionários e meio q se torna um só, para copiar se usa o modulo copy e deepcopy
