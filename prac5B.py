import pandas as pd  # For reading and cleaning tabular data

# Reading and printing CSV file data
inputData = pd.read_csv("Good-or-Bad.csv", encoding="latin-1")
print("-" * 20, "Input Data", "-" * 20)
print(inputData)
# shape[0] = number of rows, shape[1] = number of columns
print(f"No of Rows: {inputData.shape[0]}")
print(f"No of Columns: {inputData.shape[1]}")

# Manipulating data from csv file and printing the formatted result
# how - any suggests any row that has even one missing attribute must be dropped
outputData = inputData.dropna(axis=0, how="any")
print("-" * 20, "Output Data", "-" * 20)
print(outputData)
print(f"No of Rows: {outputData.shape[0]}")
print(f"No of Columns: {outputData.shape[1]}")

# Save the stricter result (only fully complete rows remain)
outputData.to_csv("FixedAny.csv", index=False)
