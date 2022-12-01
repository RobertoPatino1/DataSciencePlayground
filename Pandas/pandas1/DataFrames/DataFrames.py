import pandas as pd
#Los dataframes son estructuras de datos de 2 dimensiones. Como una matriz
#o tabla con FILAS y COLUMNAS




#Podemos crear un DataFrame a partir de un diccionario

#Esto representa 2 series. Cada clave representa un label de columna
data1 = {
    "calories":[124,178,345],
    "duration":[50,40,45]
}

#Cargando la informacion a un objeto DataFrame
#Podemos renombrar los labels con el argumento index, estos representan las filas
dataFrame1 = pd.DataFrame(data1,index=[1,2,3])
print(dataFrame1)

print("------Accediendo a las filas-----")
#Para esto debemos usar la funcion loc con el dataframe,pasando como argumento 
#la etiqueta de la fila que deseamos buscar, o una lista de etiquetas a buscar
print(dataFrame1.loc[1])
print(dataFrame1.loc[[1,3]])

#Ojo: Al usar loc con [] el resultado de la operacion tambien sera un dataframe
dataFrame1Seccionado = dataFrame1.loc[[1,3]]
print(dataFrame1Seccionado)