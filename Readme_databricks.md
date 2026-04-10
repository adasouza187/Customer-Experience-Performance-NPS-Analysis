# 📊 Análise de Vendas com Databricks (PySpark)

## 🎯 Objetivo
Este projeto tem como objetivo realizar a ingestão, transformação e análise de dados de vendas utilizando PySpark no Databricks, simulando um pipeline de dados em ambiente de Big Data.

---

## 🛠️ Tecnologias utilizadas
- Databricks
- PySpark
- Python
- GitHub

---

## 📂 Estrutura do projeto

databricks-vendas/
│
├── notebooks/
│   └── analise_vendas_databricks.py
│
├── data/
│   └── vendas.csv
│
├── outputs/
│   └── vendas_tratado.csv
│
└── README.md

---

## 🔄 Pipeline de Dados

### 1. Ingestão
Leitura do arquivo CSV armazenado no Databricks (Volumes):

```python
df = spark.read.csv('/Volumes/workspace/default/arquivos-aula/vendas.csv', header=True, inferSchema=True)
