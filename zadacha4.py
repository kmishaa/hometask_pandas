import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

res = df.isnull().max().max()
if (res == True):
    print ('Есть пропуски')
else:
    print ('Пропусков нет')
