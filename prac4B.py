import pandas as pd  # For reading and handling the dataset

inputFile = "~/notes/DS/prac/IP_DATA_ALL.csv"
# Read the CSV and force a specific data type for each column
# so numbers are stored as numbers and text/codes as strings
inputData = pd.read_csv(
    inputFile,
    low_memory=False,
    encoding="latin-1",
    dtype={
        "ID": "int",
        "Country": "str",
        "Place.Name": "str",
        "Post.Code": "str",  # Kept as string to preserve leading zeros
        "Latitude": "float",
        "Longitude": "float",
        "First.IP.Number": "float",
        "Last.IP.Number": "float",
    },
)

print("-" * 10, "Input Data", "-" * 10)
print(inputData)

# Get the list of unique countries (duplicates removed) as a new DataFrame
newInputData = pd.DataFrame({"Country": inputData["Country"].unique()})
# Build an output table with the country and a second column "PatternCountry"
# that currently holds the same values (a base for pattern/format checks)
outputData = pd.DataFrame(
    {"Country": newInputData["Country"], "PatternCountry": newInputData["Country"]}
)
