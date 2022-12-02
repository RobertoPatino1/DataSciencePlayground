import pandas as pd
dataset = pd.read_csv("pandas1/DataCleaning/files/data.csv")

print(dataset.duplicated().to_string())

#Para eliminar los duplicados usamos la funcion drop_duplicates desde el dataset

dataset.drop_duplicates(inplace = True)
print(dataset.to_string())