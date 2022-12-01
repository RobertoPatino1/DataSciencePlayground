import pandas as pd
print("------Cargando archivos a DataFrames------")
#Podemos cargar datasets contenidos en archivos a un dataframe
print("------1. Csv Files------")
#Los archivos csv presentan una forma optima de almacenar datasets

#Recuerda: Las rutas relativas inician en la carpeta raiz del proyecto
dataframeCsv1 = pd.read_csv('pandas1/DataFrames/files/data.csv')
print("---Sin to_string()---")
print(dataframeCsv1)
#OJO: Para mostrar el dataframe completo se usa la funcion to_string()
print("---Con to_string()---")
print(dataframeCsv1.to_string())