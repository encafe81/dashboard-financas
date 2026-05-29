import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração da página
st.set_page_config(page_title="Dashboard Finanças", layout="wide")

# Função auxiliar para formatação de moeda brasileira
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# 2. Carregar dados CSV (Focado exclusivamente no arquivo padrão)
@st.cache_data
def carregar_dados_csv(caminho):
    df = pd.read_csv(caminho)
    df["data"] = pd.to_datetime(df["data"])
    return df

# Título do Dashboard
st.title("📊 Dashboard de Finanças Pessoais")

# Tenta carregar a base de dados padrão
try:
    df = carregar_dados_csv("extrato_fake.csv")
except FileNotFoundError:
    st.error("Erro: O arquivo 'extrato_fake.csv' não foi encontrado. Execute o script 'gerar_dados.py' primeiro para criar a base de dados.")
    st.stop()

# Função para categorizar os lançamentos fictícios
def categorizar(texto):
    texto = str(texto).upper()
    if "SUPERMERCADO" in texto: return "Alimentação"
    elif "FARMA" in texto: return "Saúde"
    elif "POSTO" in texto or "ESTAC" in texto: return "Transporte"
    elif "SALARIO" in texto: return "Receitas"
    else: return "Outros"

df["categoria"] = df["lançamentos"].apply(categorizar)

# ==========================================
# BARRA LATERAL (FILTROS)
# ==========================================
st.sidebar.header("⚙️ Filtros do Dashboard")

# Definição de limites para os seletores de data
min_data = df["data"].min()
max_data = df["data"].max()

data_inicio = st.sidebar.date_input("Data início:", value=min_data, min_value=min_data, max_value=max_data)
data_fim = st.sidebar.date_input("Data fim:", value=max_data, min_value=min_data, max_value=max_data)

# Seleção múltipla de categorias
categorias_unicas = df["categoria"].unique()
categorias_selecionadas = st.sidebar.multiselect("Escolha as categorias:", options=categorias_unicas, default=categorias_unicas)

# Tipo de gráfico exibido na tela principal
tipo_grafico = st.sidebar.radio("Escolha o tipo de gráfico:", ("Barras", "Linha", "Pizza"))

# ==========================================
# FILTRAGEM E RESUMO
# ==========================================
df_filtrado = df[
    (df["data"].dt.date >= data_inicio) & 
    (df["data"].dt.date <= data_fim) &
    (df["categoria"].isin(categorias_selecionadas))
].copy()

resumo = df_filtrado.groupby("categoria")["valor (R$)"].sum().reset_index()

# ==========================================
# CARTÕES DE MÉTRICAS NO TOPO
# ==========================================
receitas = df_filtrado[df_filtrado["valor (R$)"] > 0]["valor (R$)"].sum()
despesas = df_filtrado[df_filtrado["valor (R$)"] < 0]["valor (R$)"].sum()
saldo = receitas + despesas

st.subheader("💰 Resumo Financeiro")
col1, col2, col3 = st.columns(3)
col1.metric("Saldo Atual", formatar_moeda(saldo))
col2.metric("Total de Receitas", formatar_moeda(receitas))
col3.metric("Total de Despesas", formatar_moeda(despesas))

st.markdown("---")

# ==========================================
# GRÁFICOS
# ==========================================
st.subheader(f"📊 Gráfico de Gastos por Categoria ({tipo_grafico})")

if tipo_grafico == "Barras":
    st.bar_chart(data=resumo, x="categoria", y="valor (R$)")
elif tipo_grafico == "Linha":
    st.line_chart(data=resumo, x="categoria", y="valor (R$)")
else: # Opção Pizza
    resumo_pizza = resumo.copy()
    resumo_pizza["valor (R$)"] = resumo_pizza["valor (R$)"].abs()
    fig = px.pie(resumo_pizza, values="valor (R$)", names="categoria", hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# TABELA DETALHADA
# ==========================================
st.subheader("🔍 Registro Detalhado (Filtrado)")
st.dataframe(df_filtrado.head(10), use_container_width=True)