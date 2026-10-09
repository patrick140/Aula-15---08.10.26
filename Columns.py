import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.loureiro\Documents\Aulas\funcionarios.csv")

df['Lucro total'] = df['lucro'] - df['salario']

print(df)