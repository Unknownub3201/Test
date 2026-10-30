import pandas as pd  # pandas is used to read and manipulate tabular data

# Path to the input CSV file containing country codes
inputFile = "/home/misterfroopy/notes/DS/prac/practical-data-science/VKHCG/05-DS/9999-Data/Country_Code.csv"
# Read the CSV; latin-1 encoding handles special characters in country names
inputData = pd.read_csv(inputFile, encoding="latin-1")
# Input Data
print("-" * 10, "Input Data", "-" * 10)
print(inputData)

# Note: this is a reference, not a copy, so changes below also affect inputData
outputData = inputData
# Drop the columns we don't need (errors="ignore" avoids a crash if a column is missing)
outputData.drop(
    labels=["ISO-2-Code", "ISO-3-Code"], axis=1, inplace=True, errors="ignore"
)
# Output Data
# Rename columns to cleaner, more descriptive names
outputData.rename(
    columns={"Country": "CountryName", "ISO-M49": "CountryNumber"}, inplace=True
)
# Sort rows by country name in descending (Z -> A) order
outputData.sort_values(by="CountryName", ascending=False, inplace=True)
print("-" * 10, "Output Data", "-" * 10)
print(outputData)

# Save the cleaned data to a new CSV file (index=False skips the row numbers)
outputFile = "/home/misterfroopy/notes/DS/prac/journal/CSV_HORUS_COUNTRY_CODE.csv"
outputData.to_csv(outputFile, index=False)
