import pandas as pd  # For reading and handling the dataset

inputFile = "~/notes/DS/prac/IP_DATA_ALL.csv"
# low_memory=False reads the whole file at once so column types are inferred correctly
inputData = pd.read_csv(inputFile, low_memory=False, encoding="latin-1")

# Show each original column name along with its Python type
print("-" * 10, "Input Data", "-" * 10)
for i in range(len(inputData.columns)):
    print(inputData.columns[i], type(inputData.columns[i]))

print("-" * 10, "Output Data", "-" * 10)
outputData = inputData
# Clean each column name: strip spaces and replace "." with "_"
# (e.g. "Place.Name" -> "Place_Name") so names are easier to use in code/SQL
for i in range(len(inputData.columns)):
    ColumnOldName = outputData.columns[i]
    ColumnNewName = ColumnOldName.strip().replace(".", "_")
    outputData.columns.values[i] = ColumnNewName
    print(outputData.columns[i], type(outputData.columns[i]))

print("-" * 10, "Output Data with ID", "-" * 10)
outputDataID = outputData
# Name the index "RowID" so each row has a labelled unique identifier
outputDataID.index.names = ["RowID"]
print(outputDataID)

# Save the data with cleaned column names to a new CSV file
# (index=False means the RowID index is not written to the file)
outputFile = "~/notes/DS/prac/IP_DATA_ALL_NEW.csv"
outputDataID.to_csv(outputFile, index=False)
