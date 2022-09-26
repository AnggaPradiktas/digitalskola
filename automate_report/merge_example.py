import pandas as pd
df1 = pd.DataFrame({'buah': ['apel','pisang'], 'harga':[10,20]})
df2 = pd.DataFrame({'buah': ['apel','pisang', 'nanas'], 'harga':[10,20,30]})
pd.merge(df1, df2, on=['buah','harga'], how='inner')