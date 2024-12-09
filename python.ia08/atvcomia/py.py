def produto_mais_vendido(vendas):
    if not vendas:
        return []

    max_vendas = max(vendas.values())

    produtos_mais_vendidos = [produto for produto, quantidade in vendas.items() if quantidade == max_vendas]
    
    return produtos_mais_vendidos

def obter_vendas_do_usuario():
    vendas = {}
    
    while True:
        produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")
        
        if produto.lower() == 'fim':
            break

        try:
            quantidade = int(input(f"Digite a quantidade vendida de '{produto}': "))
            vendas[produto] = quantidade
        except ValueError:
            print("Por favor, insira um número válido para a quantidade.")
    
    return vendas

def main():
    print("Bem-vindo ao sistema de vendas!")

    vendas = obter_vendas_do_usuario()
    
    if vendas:
        produtos_mais_vendidos = produto_mais_vendido(vendas)
        print("Os produtos mais vendidos são:", produtos_mais_vendidos)
    else:
        print("Nenhum produto foi registrado.")
    
if __name__ == "__main__":
    main()
