import pandas as pd 


df = pd.DataFrame({'Job Position':['CEO', 'Senior Manager', 'Junior Manager', 'Employee', 'Assitant Staff'], 'Years of Experience':[5, 4, 3, None, 1], 'Salary':[100_000, 80_000, None, 40_000, 20_000]})

 # df = pd.read_csv()
print(f"Original Dataset:\n  {df}")

df['Years of Experience'].fillna(df['Years of Experience'].median(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print(f"After Handling Missing Values and outliers:\n {df}")

# filtering data 
df_filtered = df[df['Years of Experience'].notnull()]

# Sorting data 
df_sorted = df.sort_values(by='Salary', ascending=False)

# Grouping  
df_group = df.groupby('Job Position')['Salary'].mean().reset_index()

print("Original Data Frame: ")
print(df.head())
print("Filtered Data Frame: ")
print(df_filtered)
print("Sorted Data Frame: ")
print(df_sorted)
print("Grouped Data Frame: ")
print(df_group)
