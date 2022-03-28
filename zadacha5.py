import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

print ('Экзамен: среднее значение')
for i in range(1, 4):
    print (df.columns[i + 6], df.mean()[i])
