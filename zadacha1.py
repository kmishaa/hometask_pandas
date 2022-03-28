import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

df.pop('index')
print(df.iloc[0:10])
