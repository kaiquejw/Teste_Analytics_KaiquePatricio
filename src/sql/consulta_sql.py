import sqlite3
import pandas as pd


df = pd.read_csv("data/data_clean.csv")


conn = sqlite3.connect(":memory:")
df.to_sql("vendas", conn, index=False, if_exists="replace")


# Query 1: Total de vendas por produto

query1 = """
SELECT 
    produto,
    categoria,
    SUM(quantidade * preco) AS total_vendas
FROM vendas
GROUP BY produto, categoria
ORDER BY total_vendas DESC;
"""

print(" Total de vendas por produto ")
print(pd.read_sql_query(query1, conn))



# Query 2: Produtos que venderam menos em junho de 2023

query2 = """
SELECT 
    produto,
    SUM(quantidade) AS total_unidades
FROM vendas
WHERE data >= '2023-06-01' AND data < '2023-06-30'
GROUP BY produto
ORDER BY total_unidades ASC;
"""

print(" Produtos que venderam menos em junho de 2023 ")
print(pd.read_sql_query(query2, conn))

# 4. Fechar conexão
conn.close()
