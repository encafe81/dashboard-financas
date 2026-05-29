# 📊 Dashboard de Finanças Pessoais

Dashboard interativo em Python para análise de finanças pessoais. O projeto automatiza a limpeza, transformação e categorização de dados financeiros (baseados no padrão de extratos bancários do Itaú) utilizando a biblioteca Pandas, transformando dados brutos em insights visuais claros de receitas e despesas.

> **Nota sobre o Portfólio:** Para garantir a estabilidade da aplicação para os avaliadores, o dashboard atualmente consome uma base de dados sintética (`extrato_fake.csv`) gerada automaticamente, simulando o layout real de um extrato sem expor dados sensíveis.

## 🚀 Funcionalidades
* **Filtros Dinâmicos:** Filtragem de lançamentos por período de datas e múltiplas categorias.
* **Categorização Automática:** Lógica Python que lê a descrição do lançamento e atribui categorias (Alimentação, Transporte, Saúde, etc.).
* **Métricas em Tempo Real:** Cartões (KPIs) exibindo Saldo Atual, Receitas e Despesas.
* **Visualização de Dados:** Gráficos interativos (Barras, Linhas e Pizza) gerados com Plotly e Streamlit.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12+**
* **Pandas:** Para manipulação, agregação e limpeza dos dados (ETL).
* **Streamlit:** Para a construção da interface web interativa.
* **Plotly:** Para a renderização dos gráficos.
* **Numpy:** Para a geração dos dados sintéticos de teste.

## ⚙️ Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/dashboard-financas.git](https://github.com/SEU_USUARIO/dashboard-financas.git)
   cd dashboard-financas