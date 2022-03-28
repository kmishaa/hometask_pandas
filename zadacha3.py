import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

print ('Столбцы: ', 'минимум,', 'максимум,', 'среднее значение,', 'стандартное отклонение')
for i in range(0, 4):
    d = i
    if (i>0):
        d += 6
    print (df.columns[d], df.min()[d], df.max()[d], df.mean()[i], round(df.std()[i], 3))
