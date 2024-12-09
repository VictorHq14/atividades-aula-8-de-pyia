def contar_pares_e_impares(lista):
    pares = len(list(filter(lambda x: x % 2 == 0, lista)))
    impares = len(list(filter(lambda x: x % 2 != 0, lista)))
    
    return pares, impares

def main():
    numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
    
    pares, impares = contar_pares_e_impares(numeros)
    
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

if __name__ == "__main__":
    main()





