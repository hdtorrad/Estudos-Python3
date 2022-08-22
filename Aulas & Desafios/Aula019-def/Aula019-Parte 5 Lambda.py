"""
def lambda, função anonima e uso para ordenação de listas
"""
l1 = [
    ['005', 548],
    ['075', 151],
    ['054', 454]
]

print(sorted(l1, key=lambda i: i[1], reverse=True))