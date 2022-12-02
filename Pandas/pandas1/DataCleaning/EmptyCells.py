import pandas as pd
print("------Cleaning empty cells------")


#Un approach puede ser borrar las filas que contienen a las celdas vacias
#Esto es ideal solo si el dataset contiene muchos registros
dataset = pd.read_csv("pandas1/DataCleaning/files/data.csv")
print(dataset.to_string())
print("\n1. Eliminando las filas con valores nulos\n")
#Podemos usar la funcion dropna, esta se llama a partir del dataset original y crea un nuevo dataset 
#con las filas vacias eliminadas
#DataFrame.dropna(*, axis=0, how=_NoDefault.no_default, thresh=_NoDefault.no_default, subset=None, inplace=False)[source]

#OJO: Esto elimina por completo la fila, incluyendo su label
cleanedDF = dataset.dropna()
print(cleanedDF.to_string())

#Para cambiar el dataset OG podemos pasar como argumento a la funcion el parametro inplace = true
#dataset.dropna(inplace = True)



print("\n2. Asignandole un nuevo valor a las celdas vacias\n")
cleanedDF2 = dataset.fillna(30)
print(cleanedDF2.to_string())

print("\nAsignandole un nuevo valor solo a ciertas columnas")
cleanedDF3 = dataset["Calories"].fillna(130)
print(cleanedDF3.to_string())



print("\n3. Reemplazar el valor con la media/moda/mediana\n")

#dataset.mean()-> Promedio/Media
#dataset.median()-> Mediana
#dataset.mode()-> Moda

promedio = round(dataset["Calories"].mean(),2)
print(promedio)
cleanedDF4 = dataset.fillna(promedio)
print(cleanedDF4.to_string())

mediana = round(dataset["Calories"].median(),2)
cleanedDF5 = dataset.fillna(mediana)

moda = dataset["Calories"].mode()[0]
cleanedDF6 = dataset.fillna(moda)