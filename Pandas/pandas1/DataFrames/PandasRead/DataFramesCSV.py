import pandas as pd
print("------Cargando archivos CSV a DataFrames------")
#Podemos cargar datasets contenidos en archivos a un dataframe
print("------1. Carga------")
#Los archivos csv presentan una forma optima de almacenar datasets

#Recuerda: Las rutas relativas inician en la carpeta raiz del proyecto
dataframeCsv1 = pd.read_csv('pandas1/DataFrames/files/data.csv')
print("---Sin to_string()---")
print(dataframeCsv1)
#OJO: Para mostrar el dataframe completo se usa la funcion to_string()
print("---Con to_string()---")
print(dataframeCsv1.to_string())


print("------2. Cambiar el total maximo de filas a leer------")
#Esto sirve para evitar usar la funcion to_string()
pd.options.display.max_rows = 9999
print(pd.options.display.max_rows)
print(dataframeCsv1)