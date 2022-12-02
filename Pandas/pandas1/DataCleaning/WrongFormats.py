import pandas as pd
print("------Cleaning data with wrong formats------")
#Podemos eliminar las filas o convertirlas al formato adecuado
dataset = pd.read_csv("pandas1/DataCleaning/files/data.csv")
#Convirtiendo al formato adecuado toda la columna Date
#dataset['Date'] = pd.to_datetime(dataset['Date'])
print(dataset.to_string())



print("Reemplazando los datos")
promedio = dataset["Duration"].mean()
for x in dataset.index:
    if(dataset.loc[x,'Duration']>90):
        dataset.loc[x,'Duration'] = promedio

print(dataset.to_string())