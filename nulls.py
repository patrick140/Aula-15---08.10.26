import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.loureiro\Documents\Aulas\funcionarios.csv")
dfNull = pd.read_csv(r"C:\Users\patrick.loureiro\Documents\Aulas\funcionarios - Null.csv")

print(dfNull.isna().sum())

dfNullRemovido = dfNull.dropna(subset=['departamento']) #remove as linhas com valores nulos

dfNullPreenchido = dfNull.fillna("nenhum") #preenche as linhas vazias com um valor especifico

#dfNullPreenchido['departamento'] = dfNullPreenchido['departamento'].fillna("nenhum") #para so preencher os valores nulos de uma coluna especifica

dfNullPreenchido = dfNullPreenchido.fillna({'departamento': "nenhum", 'lucro': 0}) 

print(dfNullPreenchido.info())
print("\n")
print(dfNullRemovido.info())


#-----------------------------------------------------------------------------------------------------------------------------#
#exemplos de tipos 
""" df['col'].astype('int')
df['col'].astype('float')
df['col'].astype('str')
df['col'].astype('bool') """

dfTrocadoTipo = dfNullPreenchido

dfTrocadoTipo['ativo'] = dfTrocadoTipo['ativo'].astype('str')

dfTrocadaData = dfNullPreenchido 

dfTrocadaData['data de nascimento'] = pd.to_datetime(dfTrocadaData['data de nascimento'])

#caso a data esteja em formato brasileiro use : dfTrocadaData['data de nascimento'] = pd.to_datetime(df['data de nascimento'], format='%d/%m/%Y')

print(dfTrocadaData.info())