"""
Tuplas- Diferença entre elas e listas é q elas não são modificaveis
"""

t1 = 1, 3, 4, 5
t2 = 2, 5, 7527, 27, 5
t3 = t1 + t2
print(type(t1))
print(type(t2))
print(t3)

t1 = list(t1)
t1[2] = 2
t1 = tuple(t1)

print(t1, type(t1))