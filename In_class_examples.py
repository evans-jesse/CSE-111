import pandas as pd
df = pd.read_cvs("w09water.csv")
print(df.describe())