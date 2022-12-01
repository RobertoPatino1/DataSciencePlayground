import pandas as pd

#El numero de elementos en cada renglon del dataset debe ser el mismo
#para todos los casos
myDataset = {"cars":["BMW","Ferrari","Chevrolet","Tesla"],
"passings": [1,2,3,4]
}

myVar = pd.DataFrame(myDataset)

#print(myVar)

print("------Creating a series------")

serie1 = pd.Series(["this","is","a","series"])
print(serie1)
