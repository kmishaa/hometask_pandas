import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

passmark = 50

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

mas = []
for i in range(0, len(df)):
    if (df['math score'][i] < passmark or df['math score'][i] < passmark or df['writing score'][i] < passmark):
        mas.append('F')
    else:
        mas.append('P')

df['OverAll_PassStatus'] = mas

print (df)
