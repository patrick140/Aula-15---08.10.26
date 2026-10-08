import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.araujo\OneDrive - SENAC-ARRJ\Documentos\Analista de dados\funcionarios.csv")
dfNull = pd.read_csv(r"C:\Users\patrick.araujo\OneDrive - SENAC-ARRJ\Documentos\Analista de dados\funcionarios - Null.csv")

dfNullRemovido = dfNull.dropna(subset=['departamento']) #remove as linhas com valores nulos

dfNullPreenchido = dfNull.fillna("nenhum") #preenche as linhas vazias com um valor especifico

#dfNullPreenchido = dfNull['departamento'].fillna("nenhum") #para so preencher os valores nulos de uma coluna especifica

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