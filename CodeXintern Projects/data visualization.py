import matplotlib.pyplot as plt

dept_count = df['Department'].value_counts()
print("Number of employees in each department: \n",dept_count)


plt.figure(figsize=(10, 6))
plt.pie(dept_count, labels=dept_count.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Employees by Department')
plt.show()

# Example: Creating a line plot
plt.plot(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary')
plt.show()

# Example: Creating a scatter plot
plt.scatter(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary')
plt.show()

# Example: Creating a bar chart
plt.bar(dept_count.index, dept_count.values)
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.title('Number of Employees in Each Department')
plt.show()


# Example: Creating a histogram
plt.hist(df['Salary'], bins=10)
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary Distribution')
plt.show()


# Example: Creating a pie chart
plt.pie(dept_count, labels=dept_count.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Employees by Department')
plt.show()