import pandas as pd


## 📦 Importação e carga
# converter data
df = pd.read_csv(r'C:\Users\adasouza\OneDrive - Simpress\Documentos\Projeto_PY_PB\vendas.csv')

print(df.head())



##🧹 Tratamento de dados

df['Data'] = pd.to_datetime(df['Data'])

# criar coluna de faturamento
df['Faturamento_Bruto'] = df['Quantidade'] * df['Preco_Unitario']

# aplicar desconto
df['Faturamento_Liquido'] = df['Faturamento_Bruto'] * (1 - df['Desconto'])

print(df.head())


## 📊 KPIs principais

faturamento_total = df['Faturamento_Liquido'].sum()

# quantidade total vendida
quantidade_total = df['Quantidade'].sum()

# ticket médio
ticket_medio = faturamento_total / quantidade_total

print("Faturamento Total:", faturamento_total)
print("Quantidade Total:", quantidade_total)
print("Ticket Médio:", round(ticket_medio, 2))

## 📍 Análise por Região
vendas_regiao = df.groupby('Regiao')['Faturamento_Liquido'].sum().sort_values(ascending=False)
print(vendas_regiao)

##📦 Análise por Produto
vendas_produto = df.groupby('Produto')['Faturamento_Liquido'].sum().sort_values(ascending=False)
print(vendas_produto)

##🛒 Análise por Canal

vendas_canal = df.groupby('Canal')['Faturamento_Liquido'].sum()
print(vendas_canal)

## 📅 Análise temporal
vendas_por_dia = df.groupby('Data')['Faturamento_Liquido'].sum()
print(vendas_por_dia)

## 📈 Gráfico matplotlib

import matplotlib.pyplot as plt

vendas_regiao.plot(kind='bar')
plt.title('Faturamento por Região')
plt.xlabel('Região')
plt.ylabel('Faturamento')
plt.show()
