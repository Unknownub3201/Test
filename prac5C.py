import pandas as pd  # For creating and cleaning the table
import numpy as np  # np.nan is used to represent missing values

# Student marks in three subjects; np.nan means the mark is missing
data = {
    "Name": ["John", "Doe", "Annie", "Alex", "Walter"],
    "Soft Computing": [90, np.nan, 75, np.nan, 89],
    "Data Science": [np.nan, np.nan, 80, 70, 84],
    "Cloud Computing": [100, 75, np.nan, np.nan, 88],
}

df = pd.DataFrame(data)
print("-" * 10, "Input Data", "-" * 20)
print(df)

# dropna(thresh=N) keeps only rows that have at least N non-null values
# (the Name column counts too, so each row has a maximum of 4 non-nulls)
print("-" * 20, "Output Data with at least 2 non-null values", "-" * 20)
print(df.dropna(thresh=2))
print("-" * 20, "Output Data with at least 3 non-null values", "-" * 20)
print(df.dropna(thresh=3))
print("-" * 20, "Output Data with at least 4 non-null values", "-" * 20)
print(df.dropna(thresh=4))  # Only rows with no missing values survive
