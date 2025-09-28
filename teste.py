import pandas as pd
import csv

produtos = [
    {"nome": "Camisa", "categoria": "Vestuário", "preco": 5.0},
    {"nome": "Calca", "categoria": "Vestuário", "preco": 10.0},
    {"nome": "Calca", "categoria": "Vestuário", "preco": 20.0},
    {"nome": "Notebook", "categoria": "Eletrônicos", "preco": 3800.0},
    {"nome": "Geladeira", "categoria": "Eletrodomésticos", "preco": 2100.0}
]

venda = [
    {"id": 1, "produto": "Camisa", "quantidade": None, "data": "2023-01-15"},
    {"id": 2, "produto": "Notebook", "quantidade": 1, "data": "2023-01-16"},
    {"id": 3, "produto": "Calca", "quantidade": 1, "data": "2023-01-17"},
    {"id": 4, "produto": "Geladeira", "quantidade": 1, "data": "2023-01-18"}
]  

def calcular_mediana(valores):
    if not valores:
        return 0
    
    valores_ordenados = sorted(valores)
    meio = len(valores_ordenados) // 2
    
    if len(valores_ordenados) % 2 == 1:
        return valores_ordenados[meio]
    else:
        return (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2

def tratar_valores_faltantes(vendas, produtos):
    precos_validos = [p["preco"] for p in produtos if isinstance(p["preco"], (int, float))]
    quantidades_validas = [v["quantidade"] for v in vendas if v["quantidade"] is not None]

    mediana_preco = calcular_mediana(precos_validos)
    mediana_quantidade = calcular_mediana(quantidades_validas)
    
    precos_por_produto = {}
    for produto in produtos:
        if isinstance(produto["preco"], (int, float)):
            precos_por_produto[produto["nome"]] = produto["preco"]
            
    for venda in vendas:
        if venda["quantidade"] is None:
            venda["quantidade"] = mediana_quantidade
            
        if "preco" not in venda or venda["preco"] is None:
            nome_produto = venda["produto"]
            if nome_produto in precos_por_produto:
                venda["preco"] = precos_por_produto[nome_produto]
            else:
                venda["preco"] = mediana_preco
                
    return vendas

def calcular_total_vendas(vendas, produtos):

 total = 0
 for venda in vendas:
    for produto in produtos:
        if venda["produto"] == produto["nome"]:
            total += venda["preco"] * venda["quantidade"]

 return total

vendas_limpa = tratar_valores_faltantes(venda, produtos)
with open("data_clean.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=vendas_limpa[0].keys())
    writer.writeheader()
    writer.writerows(vendas_limpa)
print(calcular_total_vendas(vendas_limpa, produtos))
precos = [p["preco"] for p in produtos if isinstance(p["preco"], (int, float))]
print(precos)  
print(calcular_mediana(precos))
input("Pressione enter para sair") 