import pandas as pd 

# Lê o arquivo CSV que geramos e armazena os dados na variável df
df = pd.read_csv("extrato_fake.csv")

# Exibe as primeiras 5 linhas da tabela no terminal para conferirmos
print(df.head())

# Função que define a categoria com base no texto do lançamento
def categorizar(texto):
    if "SUPERMERCADO" in texto:
        return "Alimentação"
    elif "FARMA" in texto:
        return "Saúde"
    elif "ESTAC" in texto or "POSTO" in texto:
        return "Transporte"
    elif "SALARIO" in texto:
        return "Receitas"
    else:
        return "Outros"

# Cria a nova coluna 'categoria' aplicando a função linha por linha
df["categoria"] = df["lançamentos"].apply(categorizar)

# Exibe as primeiras 5 linhas com a nova coluna para testarmos
print(df.head())

# Agrupa os dados por categoria e soma os valores de cada uma
resumo_categorias = df.groupby("categoria")["valor (R$)"].sum().reset_index()

# Exibe o resultado consolidado no terminal
print("\n--- RESUMO DE GASTOS POR CATEGORIA ---")
print(resumo_categorias)

import matplotlib.pyplot as plt

# Define o estilo e cria o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(resumo_categorias["categoria"], resumo_categorias["valor (R$)"], color=["tomato", "cornflowerblue", "mediumseagreen", "orange", "grey"])

# Adiciona títulos e etiquetas decorativas
plt.title("Balanço Financeiro por Categoria (2025)", fontsize=14, fontweight="bold")
plt.xlabel("Categorias", fontsize=12)
plt.ylabel("Valor Total (R$)", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Guarda o gráfico como uma imagem real no Codespaces
plt.savefig("grafico_financas.png", dpi=300, bbox_inches="tight")
print("\n🚀 Gráfico gerado e guardado com sucesso como 'grafico_financas.png'!")