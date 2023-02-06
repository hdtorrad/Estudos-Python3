#Crie uma lista de compras
import os

print("Bem-Vindo a sua lista de compras!\n")
lista_compra = []

while True:
    opcao = input("Insira o que deseja fazer:\n\n[i]inserir \t[a]pagar \t[l]istar: ").strip().lower()[0]
    
    if opcao == 'i':
        produto_insercao = input("\nInsira o nome do produto a ser inserido na lista: ")
        lista_compra.append(produto_insercao)
        
        os.system("cls")
        print("\nProduto adicionado com sucesso!")
    
    elif opcao == 'a':    
        produto_del = input("Insira o index ou o nome do produto a ser apagado: ")
        
        if produto_del.isdigit():
            try:
                lista_compra.pop(int(produto_del))
                
                os.system("cls")
                print("Produto excluido com sucesso!!")
            except IndexError:
                os.system("cls")
                print("\nErro ao tentar apagar!")
            
        else:
            try:
                lista_compra.remove(produto_del)

                os.system("cls")
                print("Produto excluido com sucesso!!")
            except:
                os.system("cls")
                print("\nErro ao tentar apagar!")
    
    elif opcao == 'l':

        os.system("cls")

        if len(lista_compra) > 0 :

            for indice, valor in enumerate(lista_compra):
                if indice == 0:
                    print("Lista de Compras:\n")
                print(indice, valor)
        
        else:
            print("Lista Vazia!")

    else:

        os.system("cls")
        print("Opção Inválida!")

    os.system("pause")