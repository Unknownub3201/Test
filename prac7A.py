import pandas as pd  # For running SQL queries into DataFrames and writing them back
import sqlite3 as sq  # For connecting to SQLite databases

# Connect to the source database (data warehouse)
DataBaseName1 = "datawarehouse.db"
Connection1 = sq.connect(DataBaseName1)

# Connect to the destination database (data mart)
DataBaseName2 = "datamart.db"
Connection2 = sq.connect(DataBaseName2)

# Square brackets let SQLite handle the "-" in the table name
SQLQuery1 = "SELECT * FROM [Dim-BMI];"

# Load the whole Dim-BMI table into a DataFrame
inputData = pd.read_sql_query(SQLQuery1, Connection1)
print("-" * 20, "Input Data", "-" * 20)
print(inputData)

# Select only the needed columns, ordered by PersonID
# This is the "horizontal" layout: one row per person, one column per measure
SQLQuery2 = """
SELECT PersonID, Height, Weight, BMI, Indicator
FROM [Dim-BMI]
ORDER BY PersonID;
"""

processData = pd.read_sql_query(SQLQuery2, Connection1)
print("-" * 20, "Horizontal Data", "-" * 20)
print(processData)
# Save the result into the data mart as a new table (replace it if it already exists)
processData.to_sql("Dim-BMI-Horizontal", Connection2, if_exists="replace", index=False)

# Read the table back from the data mart to confirm it was saved correctly
SQLQuery3 = "SELECT * FROM [Dim-BMI-Horizontal];"
outputData = pd.read_sql_query(SQLQuery3, Connection2)
print("-" * 20, "Output Data", "-" * 20)
print(outputData)
# Close both database connections
Connection1.close()
Connection2.close()
