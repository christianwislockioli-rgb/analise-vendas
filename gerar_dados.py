import pandas as pd
import numpy as np
import os

# Garantir que a pasta data existe
os.makedirs('data', exist_ok=True)

# Gerar dados fictícios
np.random.seed(42)
df = pd.DataFrame({
    'data': pd.date_range('2024-01-01', periods=100),
    'produto': np.random.choice(['A', 'B', 'C'], 100),
    'valor': np.random.uniform(10, 100, 100),
    'quantidade': np.random.randint(1, 10, 100)
})

# Salvar na pasta data
df.to_csv('data/vendas.csv', index=False)
print("✅ Dataset criado com sucesso: data/vendas.csv")