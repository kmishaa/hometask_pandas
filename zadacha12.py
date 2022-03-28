import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

passmark = 50

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

result = pd.pivot_table(df, columns = ['gender', 'parental level of education'])
print (result.drop(index = ['index']))
