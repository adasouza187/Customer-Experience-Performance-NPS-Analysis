%python
# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, month, year

# criar sessão
spark = SparkSession.builder.getOrCreate()

# carregar dados
df = spark.read.csv('/Volumes/workspace/default/arquivos-aula/vendas.csv', header=True, inferSchema=True)

display(df)

%md
🧹 Tratamento

%python
from pyspark.sql.functions import col

df = df.withColumn("Faturamento_Bruto", col("Quantidade") * col("Preco_Unitario"))

df = df.withColumn("Faturamento_Liquido",
                   col("Faturamento_Bruto") * (1 - col("Desconto")))

%python
# vendas por região
df.groupBy("Regiao") \
  .agg(sum("Faturamento_Liquido").alias("Total")) \
  .display()

%python
df = df.withColumn("Mes", month("Data"))
df = df.withColumn("Ano", year("Data"))

df.groupBy("Ano", "Mes") \
  .agg(sum("Faturamento_Liquido").alias("Total")) \
  .display()

%python
df.toPandas().to_csv('/Volumes/workspace/default/arquivos-aula/vendas.csv', index=False)
