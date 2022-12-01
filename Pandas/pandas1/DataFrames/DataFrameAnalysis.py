import pandas as pd
print("------Analizando la informacion------")
dataFrame = pd.read_csv("pandas1/DataFrames/files/data.csv")


print("1. Head")
#Esta funcion retorna los headers y un numero especifico de filas desde arriba
#Recibe como parametro el total de filas a seccionar

print("---Presentando las 10 primeras filas del DataFrame---")
print(dataFrame.head(10))
#Esto nos mostrara algunas cosas:
#1. El total de filas y columnas del DataSet
#2. El nombre de cada columna junto con los tipos de datos
#3. Valores no nulos en cada columna. 
#Los valores nulos deben ser removidos en la limpieza de los datos
print()
print("2. Tail")
#Sintaxis similar a la funcion head, solo que retorna las ultimas filas del DataFrame y los headers
#Recibe como parametro el total de filas a seccionar
print("---Presentando las 5 ultimas filas del DataFrame---")
print(dataFrame.tail(5))



print()
print("----Informacion sobre los datos----")
#Podemos obtener informacion del dataset con la funcion info
print(dataFrame.info())