import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados (o .. serve para voltar uma pasta e entrar na pasta data)
df = pd.read_csv('data/vendas.csv')

# Análise básica
print("Resumo estatístico:")
print(df.describe())
print(f"\nTotal de vendas: R$ {df['valor'].sum():.2f}")