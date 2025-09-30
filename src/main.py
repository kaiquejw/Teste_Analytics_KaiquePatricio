import csv
import random
import datetime
import os

# Flag para controlar se gera novos dados ou apenas lê o CSV já existente
GERAR_DADOS = False  

produtos = [
    {"nome": "Camisa", "categoria": "Vestuario", "preco": 50.0},
    {"nome": "Camisa", "categoria": "Vestuario", "preco": None},
    {"nome": "Calca", "categoria": "Vestuario", "preco": 100.0},
    {"nome": "Notebook", "categoria": "Eletronicos", "preco": 3800.0},
    {"nome": "Geladeira", "categoria": "Eletrodomesticos", "preco": 2100.0}
]

caminho_csv = "data/data_clean.csv"


# 1. GERAÇÃO DOS DADOS (só roda se GERAR_DADOS = True)

if GERAR_DADOS:
    # Simulando 50 vendas 
    vendas = []
    for i in range(1, 51): 
        produto = random.choice(produtos)
        data = datetime.date(2023, 1, 1) + datetime.timedelta(days=random.randint(0, 364))
        quantidade = random.choice([random.randint(1, 51), None])
        vendas.append({
            "id": i,
            "produto": produto["nome"],             
            "categoria": produto["categoria"],
            "quantidade": quantidade,
            "preco": produto["preco"],
            "data": str(data)
        })

    # Removendo duplicatas por id
    ids_vistos = set()
    vendas_unicas = []
    for v in vendas:
        if v["id"] not in ids_vistos:
            vendas_unicas.append(v)
            ids_vistos.add(v["id"])
            
    # Tratamento de valores nulos
    for v in vendas_unicas:
        if v["quantidade"] is None:
            v["quantidade"] = medianas.get(v["produto"], 1) 
        

    precos_catalogo = {p["nome"]: p["preco"] for p in produtos if p["preco"] is not None}
    for v in vendas_unicas:
        if v["preco"] is None:
            v["preco"] = precos_catalogo.get(v["produto"], 0.0)

    # Convertendo tipos
    for v in vendas_unicas:
        v["id"] = int(v["id"])
        v["quantidade"] = int(v["quantidade"])
        v["preco"] = float(v["preco"])

    # Salvando no CSV

    with open(caminho_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=vendas_unicas[0].keys())
        writer.writeheader()
        writer.writerows(vendas_unicas)


# 2. LEITURA DO CSV

with open(caminho_csv, "r") as f:
    reader = csv.DictReader(f)
    vendas = [row for row in reader]

# Convertendo tipos ao ler
for v in vendas:
    v["id"] = int(v["id"])
    v["quantidade"] = int(v["quantidade"])
    v["preco"] = float(v["preco"])


# 3. Total de vendas por produto

totais_valor = {}
totais_qtd = {}

for v in vendas:
    valor = v["preco"] * v["quantidade"]
    if v["produto"] not in totais_valor:
        totais_valor[v["produto"]] = valor
        totais_qtd[v["produto"]] = v["quantidade"]
    else:
        totais_valor[v["produto"]] += valor
        totais_qtd[v["produto"]] += v["quantidade"]

print("Total de vendas em R$ por produto:")
for produto, total in totais_valor.items():
    print(f"{produto}: {total:.2f}")

print("\nTotal de unidades vendidas por produto:")
for produto, qtd in totais_qtd.items():
    print(f"{produto}: {qtd}")

# Produto campeão
campeao_valor = max(totais_valor, key=totais_valor.get)
print(f"\nProduto com o maior faturamento: {campeao_valor} ({totais_valor[campeao_valor]:.2f})")

campeao_qtd = max(totais_qtd, key=totais_qtd.get)
print(f"Produto com mais unidades vendidas: {campeao_qtd} ({totais_qtd[campeao_qtd]} unidades)")
