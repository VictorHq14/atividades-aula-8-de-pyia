produtos = {
    1: {'nome': 'Arroz', 'preço': 10.50, 'quantidade': 100},
    2: {'nome': 'Carne', 'preço': 20.00, 'quantidade': 50},
    3: {'nome': 'Banana', 'preço': 5.99, 'quantidade': 200}
}

def adicionar_produto():
    id_produto = int(input("Digite o ID do produto: "))
    if id_produto not in produtos:
        nome = input("Digite o nome do produto: ")
        preço = float(input("Digite o preço do produto: R$ "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        produtos[id_produto] = {'nome': nome, 'preço': preço, 'quantidade': quantidade}
        print(f"Produto '{nome}' adicionado com sucesso!")
    else:
        print(f"Erro: O produto com ID {id_produto} já existe!")

def remover_produto():
    id_produto = int(input("Digite o ID do produto a ser removido: "))
    if id_produto in produtos:
        del produtos[id_produto]
        print(f"Produto com ID {id_produto} removido com sucesso!")
    else:
        print(f"Erro: Produto com ID {id_produto} não encontrado!")

def atualizar_produto():
    id_produto = int(input("Digite o ID do produto a ser atualizado: "))
    if id_produto in produtos:
        nome = input("Digite o novo nome do produto (deixe em branco para manter): ")
        preço = input("Digite o novo preço do produto (deixe em branco para manter): ")
        quantidade = input("Digite a nova quantidade (deixe em branco para manter): ")

        if nome:
            produtos[id_produto]['nome'] = nome
        if preço:
            produtos[id_produto]['preço'] = float(preço)
        if quantidade:
            produtos[id_produto]['quantidade'] = int(quantidade)
        
        print(f"Produto com ID {id_produto} atualizado com sucesso!")
    else:
        print(f"Erro: Produto com ID {id_produto} não encontrado!")

def exibir_produtos():
    if produtos:
        for id_produto, info in produtos.items():
            print(f"ID: {id_produto}, Nome: {info['nome']}, Preço: R${info['preço']:.2f}, Quantidade: {info['quantidade']}")
    else:
        print("Nenhum produto encontrado!")

def menu():
    while True:
        print("\nMenu de Gerenciamento de Produtos")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Atualizar produto")
        print("4. Exibir todos os produtos")
        print("5. Sair")
        
        opção = input("Escolha uma opção (1-5): ")

        if opção == '1':
            adicionar_produto()
        elif opção == '2':
            remover_produto()
        elif opção == '3':
            atualizar_produto()
        elif opção == '4':
            exibir_produtos()
        elif opção == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida (1-5).")

menu()
