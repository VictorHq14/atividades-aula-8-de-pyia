dicionario = {
    "nome": "treze",
    "altura": "dozenove",
}
while True:
    ver = input("Digite o que você gostaria de ver (nome ou altura)").lower()
    if ver == "nome" or "altura":
        print(dicionario[ver])

# esse codigo eu estava só brincando com a lógica mesmo