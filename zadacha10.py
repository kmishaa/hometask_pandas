import pandas as pd
import time

df = pd.read_csv('students_data.csv')
df.head()

passmark = 50

time_of_start = time.time()
avg = df.groupby(['race/ethnicity'])['reading score'].mean()
print('Средние баллы:')
for i in range (0, len(avg)):
    print(avg.index[i], ': ', round(avg[i], 3), sep='')
print('Потрачено:', round(time.time() - time_of_start, 5), 'секунд')

print()
time_of_second_start = time.time()
minimum = df.groupby(['parental level of education'])['writing score'].min()
print('Минимальные баллы:')
for i in range (0, len(minimum)):
    print(minimum.index[i], ': ', minimum[i], sep='')
print('Потрачено:', round(time.time() - time_of_second_start, 5), 'секунд')
