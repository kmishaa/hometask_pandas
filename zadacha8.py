import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

print ('Список столбцов:')
for i in df.columns:
    print (i)

df.rename(columns={'parental level of education': 'education'}, inplace=True)
df.rename(columns={'test preparation course': 'test preparation'}, inplace=True)

print()
print ('Список измененных столбцов:')
for i in df.columns:
    print (i)
