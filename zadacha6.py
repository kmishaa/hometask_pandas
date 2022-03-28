import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

print ('Студенты, прошедшие курс для подготовки к экзамену:')
print ('Экзамен: среднее значение')
for i in  range (1, 4):
    print (df.columns[i+6], ': ', round(df[df['test preparation course'] == 'completed'].mean()[i], 3))

print()
print ('Не прошедшие:')
print ('Экзамен: среднее значение')
for i in  range (1, 4):
    print (df.columns[i+6], ': ', round(df[df['test preparation course'] == 'none'].mean()[i], 3))
