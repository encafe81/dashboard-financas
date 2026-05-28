import pandas as pd  # Biblioteca para manipulação de tabelas (DataFrames)
import numpy as np   # Biblioteca para geração de números e operações matemáticas

# Gera uma sequência de datas diárias para o ano de 2025 inteiro
datas = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")

# Lista de lançamentos fictícios baseados no padrão do Itaú
opcoes_lancamentos = [
    "PAY SUPERMERCADO", "PAY FARMA", "PAY ESTAC", 
    "PAY POSTO COMBUSTIVEL", "PIX TRANSF", "SALARIO RECEBIDO"
]

# Sorteia um lançamento aleatório para cada um dos 365 dias do ano
lancamentos_escolhidos = np.random.choice(opcoes_lancamentos, size=len(datas))
# Cria uma lista vazia para armazenar o valor de cada dia
valores = []

# Varre a lista de lançamentos para decidir o valor de cada um
for lancamento in lancamentos_escolhidos:
    if lancamento == "SALARIO RECEBIDO":
        valores.append(5000.00)  # Valor fixo para o salário (positivo)
    else:
        # Sorteia um gasto quebrado entre R$ 10,00 e R$ 200,00 (negativo)
        gasto = round(np.random.uniform(10.00, 200.00), 2)
        valores.append(-gasto)

        # Cria a tabela organizando as listas em colunas
df = pd.DataFrame({
    "data": datas,
    "lançamentos": lancamentos_escolhidos,
    "valor (R$)": valores
})

# Calcula a coluna de saldo acumulado dia após dia
df["saldo (R$)"] = df["valor (R$)"].cumsum() + 1000.00

# Salva o resultado final num arquivo CSV sem guardar os índices
df.to_csv("extrato_fake.csv", index=False)