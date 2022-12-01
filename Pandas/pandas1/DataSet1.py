import pandas as pd

#El numero de elementos en cada renglon del dataset debe ser el mismo
#para todos los casos
myDataset = {"cars":["BMW","Ferrari","Chevrolet","Tesla"],
"passings": [1,2,3,4]
}

myVar = pd.DataFrame(myDataset)

#print(myVar)

print("------Series------")
#Una serie es como una columna de una tabla
#Contiene datos de cualquier tipo
serie1 = pd.Series(["this","is","a","series"])
print(serie1)



print("------Labels------")
#Inician en 0, se usan para acceder a valores especificos
#OJO: La indexacion no funciona en su version negativa como en las listas
print(serie1[3])


#Podemos nombrear nuestros propios labels con el argumento index al crear una serie
#Al argumento index le es asignada una lista con los nombres que tendran los nuevos indices

serie2 = pd.Series(["Honda","Chevrolet","Ferrari"],index=["x","y","z"])
print(serie2)

serie3 = pd.Series([123,56543,7654,12,32523],index= ['a','b','c','d','e'])
print(serie3)
print(serie3['d'])