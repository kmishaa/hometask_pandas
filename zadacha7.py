import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

all_values = df['lunch'].value_counts().keys()

print ('Все различные значения для столбца lunch:')
for i in all_values:
    print (i) 
