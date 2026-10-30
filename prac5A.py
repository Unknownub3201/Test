import pandas as pd  # For reading and cleaning tabular data

# Reading and printing CSV file data
inputData = pd.read_csv("Good-or-Bad.csv", encoding="latin-1")
print("-" * 10, "Input Data", "-" * 10)
print(inputData)
# shape[0] = number of rows, shape[1] = number of columns
print(f"No of Rows: {inputData.shape[0]}")
print(f"No of Columns: {inputData.shape[1]}")

# Manipulating data from csv file and printing the formatted result
# how - all suggests any row that has all missing attributes must be dropped
outputData = inputData.dropna(axis=0, how="all")
print("-" * 10, "Output Data", "-" * 10)
print(outputData)
print(f"No of Rows: {outputData.shape[0]}")
print(f"No of Columns: {outputData.shape[1]}")

# Save the cleaned data (rows that were completely empty are removed)
outputData.to_csv("FixedAll.csv", index=False)
