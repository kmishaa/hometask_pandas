import pandas as pd
import time
import numpy

df = pd.read_csv('students_data.csv')
df.head()

passmark = 50

time_of_start = time.time()
avg = {}
for i in range (0, len(df)):
    if df['race/ethnicity'][i] in avg:
        avg[df['race/ethnicity'][i]].append(df['reading score'][i])
    else:
        avg[df['race/ethnicity'][i]] = [df['reading score'][i]]
    
result = {}
for group in sorted(avg):
    result[group] = numpy.mean(avg[group])

print ('Средние баллы:')
for item in result:
    print (item, ': ', round(result[item], 5), sep='')
print('Потрачено:', round(time.time() - time_of_start, 5), 'секунд')



print()
time_of_second_start = time.time()
minimum = {}
for i in range (0, len(df)):
    if df['parental level of education'][i] in minimum:
        minimum[df['parental level of education'][i]].append(df['writing score'][i])
    else:
        minimum[df['parental level of education'][i]] = [df['writing score'][i]]
    
minimum_sorted = sorted(minimum)
result_new = {}
for group in minimum_sorted:
    result_new[group] = min(minimum[group])

print ('Минимальные баллы:')
for item in result_new:
    print (item, ': ', (result_new[item]), sep='')
print('Потрачено:', round(time.time() - time_of_start, 5), 'секунд')
