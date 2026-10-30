import pandas as pd  # Used to handle tables (DataFrame)
import xml.etree.ElementTree as ET  # Used to read and parse XML Files


# Function to convert XML to a data Frame
def xml2df(xml_data):
    root = ET.XML(xml_data)  # Convert XML String to a tree structure
    all_records = []  # Empty list to store all the records
    # Loop through each main element
    for child in root:
        record = {}  # Dictionary to store one row of data
        # Loop through each sub-element (Fields inside country tag)
        for subchild in child:
            # Store tag as key and text as value
            record[subchild.tag] = subchild.text
        all_records.append(
            record
        )  # Store each individual record into the list of records
    # Convert list of dictionaries into a dataFrame with pandas
    return pd.DataFrame(all_records)


# Path to the XML file
with open(
    # Different file path specifier for windows
    "/home/misterfroopy/notes/DS/prac/practical-data-science/VKHCG/05-DS/9999-Data/Country_Code.xml",
    "r",
    encoding="utf-8",
) as file:
    xml_content = file.read()

print("-" * 20, "Input Data Values", "-" * 20)
print(xml_content)
print("-" * 40)

# Converting the XML file to a dataframe
df = xml2df(xml_content)

# Cleaning the data Frame by removing(dropping) unwanted rows
df.drop(["ISO-2-CODE", "ISO-3-Code"], axis=1, inplace=True, errors="ignore")

# Rename the Country and ISO code
df.rename(columns={"Country": "CountryName"}, inplace=True)
df.rename(columns={"ISO-M49": "CountryNumber"}, inplace=True)

# Setting a new index
df.set_index("CountryNumber", inplace=True)

# Sorting the Data Frame
df.sort_values("CountryName", axis=0, ascending=True, inplace=True)
# Axis -> Column
# ascending -> Order in which the data is presented
# inplace -> determines whether to make changes to the data or not

print("-" * 20, "Processed Data Values", "-" * 20)
print(df)
print("-" * 40)

# File path where the csv file should be stored
df.to_csv("~/notes/DS/prac/HORUS1.csv", index=True)
