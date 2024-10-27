import pandas as pd
import numpy as np

# Leia o conteúdo do CSV fornecido
data = pd.read_csv('Database.txt', sep=';', encoding='utf-8', engine='python')

# Atribua os dados lidos a uma variável e verifique se foram importados adequadamente
# Informações gerais sobre o conjunto de dados
print("Informações gerais do conjunto de dados:")
print(data.info())
data = pd.DataFrame (data)

print("Tabela de dados")
print (data)

# Imprima as primeiras e últimas N linhas do arquivo (suponhamos N=5)
print("\nPrimeiras 5 linhas do conjunto de dados:")
print(data.head(5))
print("\nÚltimas 5 linhas do conjunto de dados:")
print(data.tail(5))

# Crie uma nova variável e atribua a ela uma cópia do conjunto de dados original
data_copy = data.copy()

# Substitua todos os valores nulos da coluna 'Calories' por 0
data_copy['Calories'].fillna(0, inplace=True)
print("\nConjunto de dados após substituir nulos em 'Calories' por 0:")
print(data_copy)

# Substitua os valores nulos da coluna 'Date' por '1900/01/01'
data_copy['Date'].fillna('1900/01/01', inplace=True)
print("\nConjunto de dados após substituir nulos em 'Date' por '1900/01/01':")
print(data_copy)

# Tente transformar a coluna 'Date' para datetime, e trate o erro se houver
try:
    data_copy['Date'] = pd.to_datetime(data_copy['Date'], format='%Y/%m/%d')
except ValueError as e:
    print("\nErro encontrado ao tentar converter 'Date' para datetime:", e)

# Substitua '1900/01/01' por NaN e tente novamente a conversão
data_copy['Date'].replace('1900/01/01', np.nan, inplace=True)
data_copy['Date'] = pd.to_datetime(data_copy['Date'], errors='coerce')

print("\nConjunto de dados após corrigir 'Date' e converter para datetime:")
print(data_copy)

# Corrija o valor específico '20201226' na coluna 'Date'
data_copy['Date'] = data_copy['Date'].replace('20201226', '2020/12/26')
data_copy['Date'] = pd.to_datetime(data_copy['Date'], errors='coerce')

# Verifique se as transformações foram aplicadas com sucesso
print("\nConjunto de dados após correções adicionais e conversão para datetime:")
print(data_copy)

# Remova registros com valores nulos (somente na coluna 'Date')
data_cleaned = data_copy.dropna(subset=['Date'])

# Imprima o dataframe final e confirme se todas as transformações foram realizadas
print("\nDataFrame final após todas as transformações:")
print(data_cleaned)
