import pandas as pd  # For running SQL queries into DataFrames and reshaping data
import sqlite3 as sq  # For connecting to SQLite databases

# Connect to the source database (data warehouse)
DatabaseName1 = (
    "/home/user/mscit/ds/practical-data-science/VKHCG/99-DW/datawarehouse.db"
)
Connection1 = sq.connect(DatabaseName1)

# Connect to the destination database (data mart)
DatabaseName2 = "/home/user/mscit/ds/practical-data-science/VKHCG/99-DW/datamart.db"
Connection2 = sq.connect(DatabaseName2)

SQLQuery1 = "SELECT * FROM [Dim-BMI];"

# Load the whole Dim-BMI table into a DataFrame
inputData = pd.read_sql_query(SQLQuery1, Connection1)
print("-" * 10, "Input Data", "-" * 10)
print(inputData)

# Select the required columns, ordered by PersonID
SQLQuery2 = """
SELECT PersonID, Height, Weight, BMI, Indicator
FROM [Dim-BMI]
ORDER BY PersonID;
"""

ProcesssedData = pd.read_sql_query(SQLQuery2, Connection1)
""" 
    Organize data vertically 
    In vertical organization:
    PersonID, and Indicator remain as columns.
    Height, Weight and BMI are converted into rows.
    Attribute column stores the name of measurements.
    Value column stores the corresponding value.
"""
# pd.melt converts the wide table into a long one:
# id_vars stay as they are, value_vars become rows of (Attribute, Value) pairs
VerticalData = pd.melt(
    ProcesssedData,
    id_vars=["PersonID", "Indicator"],
    value_vars=["Height", "Weight", "bmi"],
    var_name="Attribute",
    value_name="Value",
)

print("-" * 10, "Vertical Data", "-" * 10)
print(VerticalData)
# Save the vertical table into the data mart (replace it if it already exists)
VerticalData.to_sql("Dim-BMI-Vertical", Connection2, if_exists="replace", index=False)

SQLQeury3 = "SELECT * FROM [Dim-BMI-Vertical];"

# Read the table back from the data mart to verify it was stored correctly
outputData = pd.read_sql_query(SQLQeury3, Connection2)

print("-" * 10, "Output Data", "-" * 10)
print(outputData)
# Close both database connections
Connection1.close()
Connection2.close()
