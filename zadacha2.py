import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

print ('Размеры:', df.shape[0], 'строк и', df.shape[1], 'столбцов')
