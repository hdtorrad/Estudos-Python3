"""
SETs- Conjuntos
add- adiciona  | update- atualiza
clear- limpa  | discad- discarta
union- une ou |  | intersection & todos os elementos
presentes nos dois sets
difference ou - - elementos apenas no set da esquerda  | symetric_difference ^ elementos que estão nos dois sets,
mas não em ambos

update- Itera sobre
Set- não mantém ordem, não aceita elemento duplicado
Pode ser usado em cast de list pra tirar repitidos
"""
s = {1, 2, 3}  # Para criar um set vazio set()
print(s, type(s))

s.add(4)
s.add(5)

print(s)

s.discard(5)

print(s)

s1= {4,  5, 6, 7, 8, 9}

s2 = s | s1
s3 = s.union(s1)

print(s2, s3, sep= '\n')

s4 = s & s1

print(s4)

s5 = s - s1
s5inverted= s1 - s

print(s5, s5inverted, sep='\n')

s6 = s ^ s1

print(s6)
