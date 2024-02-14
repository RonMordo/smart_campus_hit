import pandas as pd

df = pd.read_csv('~/Documents/Projects/data_science/smart_campus_hit/data/main_data_frame_cleaned.csv')
df = df.head()
df.to_csv('PATH', index=False)