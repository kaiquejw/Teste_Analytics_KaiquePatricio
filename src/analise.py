import pandas as pd
import matplotlib.pyplot as plt


# 1. Ler o dataset limpo

df = pd.read_csv("data/data_clean.csv")


# 2. Preparar dados

# Converter coluna "data" para datetime
df["data"] = pd.to_datetime(df["data"])

# Criar coluna "mes" (ano-mês)
df["mes"] = df["data"].dt.to_period("M")

# Calcular vendas (quantidade * preço)
df["vendas"] = df["quantidade"] * df["preco"]

# Agrupar vendas por mês
vendas_mensais = df.groupby("mes")["vendas"].sum()


# 3. Plotar gráfico de linha

plt.figure(figsize=(10, 5))
vendas_mensais.plot(kind="line", marker="o", color="blue")

plt.title("Tendência de Vendas Mensais em 2023")
plt.xlabel("Mês")
plt.ylabel("Total de Vendas (R$)")
plt.grid(True)

plt.show()

""" insights a destacar:
1. Sazonalidade clara:
O gráfico mostra picos de vendas em agosto e novembro/dezembro, indicando forte relação com sazonalidade (ex.: volta às aulas, Black Friday e festas de fim de ano).

2. Meses de baixa concentração: 
Abril e junho apresentam quedas significativas, mostrando a necessidade de promoções ou campanhas específicas nesses períodos para estimular vendas.
 """

