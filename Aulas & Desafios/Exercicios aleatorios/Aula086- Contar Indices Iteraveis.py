#Contar o indice de uma lista

lista = ["Maria", 'Paula', "Andressa", 'Renata', 'Juninho', 'Bruno']
indice = 0

for i in lista:
    print(indice, i, lista.index(i)) #Existe um método para isso
    indice += 1