import pandas as pd

df = pd.read_csv('PATH')
df = df.head()
df.to_csv('PATH', index=False)