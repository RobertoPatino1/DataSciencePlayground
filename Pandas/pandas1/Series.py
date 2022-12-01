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
print(serie3['d'])  #A su ves podemos usar las etiquetas generadas para acceder al elemento correspondiente


print("------Creando series con diccionarios------")
#Usar diccionarios para crear series nos permite evitar asignar las etiquetas, ya que
#los valores correspondientes a las claves se convierten en las etiquetas de la serie
preciosFrutas = {"manzana":0.20,"pera":0.35,"naranja":1.00,"banana":0.50,"limon":0.10}

serieDict = pd.Series(preciosFrutas)
print(serieDict)

#Tambien podemos seccionar las series especificando las etiquetas que deseamos tomar
#Digamos que queremos una serie que solo contenga a manzana, banana y pera. En ese orden.
#Hariamos esto:
print("--Serie seccionada por medio de labels--")
serieDicSeccionada = pd.Series(preciosFrutas,index=["manzana","banana","pera"])
print(serieDicSeccionada)