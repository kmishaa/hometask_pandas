import pandas as pd

df = pd.read_csv('students_data.csv')
df.head()

passmark = 50
print ('Ответы:')

winners = (df[df['math score'] >= passmark]).count()
first = winners[7] / df.count()[7]
print ('1:', first)


students = df[df['test preparation course'] == 'completed']
st_winners = (students[students['math score'] >= passmark]).count()
second = st_winners[7] / students.count()[7]
print('2:', round(second, 5))

women = df[df['gender'] == 'female']
not_student_women = women[women['test preparation course'] == 'none']
wo_nost_winners = not_student_women[not_student_women['math score'] < passmark].count()
third_question = wo_nost_winners[7] / not_student_women.count()[7]
print ('3:', round(third_question, 5))
