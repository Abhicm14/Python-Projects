import pandas as pd
df = pd.read_csv('data2.csv')
print(df)

print(df.head())
print(df.tail())

print(df.describe())

mv = df.isnull().sum()
print(mv)

avg = df['Age'].mean()
print(f"Average of age: {avg}")

uv = df['Age'].nunique()
print(f"Unique values of age: {uv}")

eng_emp = df[df['Department'] == 'Engineering']
print(eng_emp)

max_Salary = df['Salary'].max()
print(f"Maximum salary: {max_Salary}")

min_Salary = df['Salary'].min()
print(f"Minimum salary: {min_Salary}")

max_Salary_emp = df[df['Salary'] == max_Salary]
print("Highest paid employee : \n", max_Salary_emp)

min_Salary_emp = df[df['Salary'] == min_Salary]
print("Lowest paid employee : \n", min_Salary_emp)

dept_count = df['Department'].value_counts()
print("Number of employees in each department: \n",dept_count)

sort = df.sort_values(by='Salary', ascending=False)
print(sort)

df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x > 30 else 'Junior')
print("Data with experience column: \n", df)
