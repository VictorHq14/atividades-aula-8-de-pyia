vendas_trimestrais = [
    [10000, 12000, 11000],
    [15000, 14000, 13000],
    [20000, 19000, 18000],  
    [25000, 24000, 23000]   
]

media_vendas_por_trimestre = [sum(trimestre) / 3 for trimestre in vendas_trimestrais]

soma_vendas_por_trimestre = [sum(trimestre) for trimestre in vendas_trimestrais]
indice_maior_soma = soma_vendas_por_trimestre.index(max(soma_vendas_por_trimestre))
maior_soma_trimestre = vendas_trimestrais[indice_maior_soma]

indice_menor_soma = soma_vendas_por_trimestre.index(min(soma_vendas_por_trimestre))
menor_soma_trimestre = vendas_trimestrais[indice_menor_soma]

total_vendas_ano = sum(soma_vendas_por_trimestre)

print("Média de vendas por trimestre:", media_vendas_por_trimestre)
print("Trimestre com maior soma de vendas:", maior_soma_trimestre)
print("Trimestre com menor soma de vendas:", menor_soma_trimestre)
print("Total de vendas no ano inteiro:", total_vendas_ano)