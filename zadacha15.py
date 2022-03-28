import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

passmark = 50

mas = []

def GetGrade(average_mark):
    if (average_mark > 90):
        mas.append('A')
    if (average_mark <= 90 and average_mark > 80):
        mas.append('B')
    if (average_mark <= 80 and average_mark > 70):
        mas.append('C')
    if (average_mark <= 70 and average_mark > 60):
        mas.append('D')
    if (average_mark <= 60 and average_mark > 50):
        mas.append('E')
    if (average_mark <= 50):
        mas.append('F')

for i in range(0, len(df)):
    avg = (df['math score'][i] + df['reading score'][i] + df['writing score'][i])/3
    GetGrade(avg)
    
df['Grade'] = mas

res = df.value_counts('Grade').sort_index()
for i in range (0, len(res)):
    print (res.index[i], ' ', res[i])    
