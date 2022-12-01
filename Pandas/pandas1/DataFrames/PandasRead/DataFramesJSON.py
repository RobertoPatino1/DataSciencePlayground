import pandas as pd
print("------Cargando archivos JSON a DataFrames------")
#Se usa la funcion read_jason, a la que se pasa como argumento la ruta del archivo json
dataFrameJson1 = pd.read_json("pandas1/DataFrames/files/data.json")
print(dataFrameJson1.to_string())