-- consultas_sql.sql
-- Dataset: tabela `vendas` com colunas
-- (id, produto, categoria, quantidade, preco, data)
-- Observação: no projeto, a tabela é criada a partir de data/data_clean.csv.

-----------------------------------------------------------------------
-- 1) Total de vendas (Quantidade * Preço) por produto + categoria,
--    ordenado do maior para o menor.
-- Lógica:
-- - Multiplica quantidade * preco para cada linha (valor da venda)
-- - Soma por produto + categoria
-- - Ordena pelo total descrescente
-----------------------------------------------------------------------
SELECT
    produto,
    categoria,
    SUM(quantidade * preco) AS total_vendas
FROM vendas
GROUP BY produto, categoria
ORDER BY total_vendas DESC;

-----------------------------------------------------------------------
-- 2) Produtos que venderam menos em junho.
-- Lógica:
-- - Filtra por mês/ano (a base gerada é de 2023)
-- - Soma as quantidades por produto
-- - Ordena do menor para o maior (os primeiros são os que menos venderam)
-- Observação: usei strftime para garantir o filtro quando `data` é TEXT.
-----------------------------------------------------------------------
SELECT
    produto,
    SUM(quantidade) AS total_unidades
FROM vendas
WHERE strftime('%Y', data) = '2023'  -- ajuste para 2024 se a base for 2024
  AND strftime('%m', data) = '06'
GROUP BY produto
ORDER BY total_unidades ASC;
