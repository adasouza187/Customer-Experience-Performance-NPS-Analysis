import pandas as pd
import matplotlib.pyplot as plt

## 📂 2. Carregamento

df = pd.read_csv(r'C:\Users\adasouza\OneDrive - Simpress\Documentos\Projeto_PY_PB\vendas.csv')

## 🧹 3. Tratamento

df['Data'] = pd.to_datetime(df['Data'])

df['Faturamento_Bruto'] = df['Quantidade'] * df['Preco_Unitario']
df['Faturamento_Liquido'] = df['Faturamento_Bruto'] * (1 - df['Desconto'])

# criar colunas temporais
df['Ano'] = df['Data'].dt.year
df['Mes'] = df['Data'].dt.month
df['Mes_Ano'] = df['Data'].dt.to_period('M')

## 📊 KPIs Estratégicos

faturamento_total = df['Faturamento_Liquido'].sum()
ticket_medio = df['Faturamento_Liquido'].mean()
total_pedidos = len(df)

print("Faturamento Total:", faturamento_total)
print("Ticket Médio:", round(ticket_medio, 2))
print("Total de Pedidos:", total_pedidos)


## 📅 Crescimento ao longo do tempo

vendas_mensais = df.groupby('Mes_Ano')['Faturamento_Liquido'].sum()

crescimento = vendas_mensais.pct_change() * 100

print(crescimento)

## 🏆 Ranking de Regiões

ranking_regiao = df.groupby('Regiao')['Faturamento_Liquido'].sum().sort_values(ascending=False)

print(ranking_regiao)

## 📊 Participação por Produto

mix_produto = df.groupby('Produto')['Faturamento_Liquido'].sum()

mix_percentual = (mix_produto / mix_produto.sum()) * 100

print(mix_percentual.sort_values(ascending=False))

## 🛒 8. Performance por canal

canal = df.groupby('Canal')['Faturamento_Liquido'].agg(['sum', 'mean'])

print(canal)

## 💸 Impacto do Desconto

desconto = df.groupby('Desconto')['Faturamento_Liquido'].mean()

print(desconto)

print(vendas_mensais)

## 📉 10. Gráfico de tendência

vendas_dia = df.groupby('Data')['Faturamento_Liquido'].sum()

vendas_dia.plot(marker='o')
plt.title('Vendas por Dia')
plt.show()

## 💾 11. Exportação
df.to_csv('vendas_tratado.csv', index=False)