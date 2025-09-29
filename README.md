# Este repositório contém a resolução do Teste de Estagiário de Analytics - Quod

1. Geração e limpeza de um dataset simulado de vendas (2023)
2. Análise exploratória com gráfico de linha mensal
3. Consultas SQL executadas sobre o dataset limpo


# Estrutura do repositório


├── README.md
├
├── data/
├
│   └── data_clean.csv          # dataset limpo gerado por main.py
├
├── src/
├   │
│   ├── main.py   # simula dados, limpa, exporta CSV (Parte 1)
│   │              
│   └── analise.py              # gráfico de linha por mês (Parte 2)
│
└── sql/
    │
    └── consulta_sql.py         # executa consultas SQL no CSV (SQLite em memória)


# Requisitos

Python 3.8+
Pacotes necessários:
  ```bash
 pip install pandas matplotlib


# Extensões

- **SQLTools (VS Code)**: útil para rodar consultas `.sql` diretamente no editor.
- Instale a extensão “SQLTools”.
- Observação: os scripts Python (`sql/consulta_sql.py`) **não dependem** dessa extensão — ela serve apenas para execução interativa das queries dentro do VS Code.

## Como executar

1. Gerar e limpar os dados (Parte 1):

Cria 50 vendas aleatórias no período 01/01/2023–31/12/2023, trata faltantes, remove duplicatas, converte tipos e salva em data/data_clean.csv.  

   ```bash
   python src/main.py

Saídas no terminal:
Total de vendas (R$) por produto
Total de unidades por produto
Produto campeão em valor e em quantidade


2. Análise exploratória – gráfico de linha (Parte 2):

Lê data/data_clean.csv, agrega por mês e plota a tendência de vendas mensais.

   ```bash
   python src/analise.py


3. Consultas SQL:

Carrega data/data_clean.csv em uma tabela vendas (SQLite em memória) e executa as queries pedidas.

   ```bash
   python sql/consulta_sql.py

Consultas implementadas:

Total de vendas por produto (R$), ordenado do maior para o menor
Produtos que venderam menos em junho de 2023

# Mais informações

1. Limpeza aplicada:

Duplicatas: removidas por id
Faltantes:
   a) quantidade = None → substituída por 1
   b)preco = None → preenchido com o preço do catálogo do produto
Tipos: id (int), quantidade (int), preco (float)
Exportação: data/data_clean.csv


2. Observações finais:

O projeto foi organizado para facilitar a avaliação: src (código), data (dados), sql (consultas).

Caso prefira rodar tudo de uma vez, execute na ordem:

python src/main.py
python src/analise.py
python sql/consulta_sql.py
