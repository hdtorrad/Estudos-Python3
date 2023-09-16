# copy, sorted, produtos.sort
# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

novos_produtos = [{**produto, 'preco': round(produto['preco'] * 1.1)} for produto in produtos]
print(novos_produtos, end='\n\n')
print(produtos, end='\n\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(sorted(novos_produtos, key= lambda produto: produto['nome']))
print(produtos_ordenados_por_nome, end='\n\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(sorted(novos_produtos, key= lambda produto: produto['preco']))
print(produtos_ordenados_por_preco, end='\n\n')