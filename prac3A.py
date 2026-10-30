import string as s  # Provides s.printable, the set of printable ASCII characters
import datetime as dt  # Used for working with dates

# --- Cleaning 1: remove leading/trailing whitespace ---
print("-" * 10, "Removing Leading or Lagging spaces from a data entry", "-" * 10)
badData = "       Data with too many spaces is bad!                  "
print(f"Bad Data: <{badData}>")
# strip() removes spaces from both ends of the string
cleanData = badData.strip()
print(f"Clean Data: <{cleanData}>")

# --- Cleaning 2: remove non-printable (control) characters ---
print("-" * 10, "Removing nonprintable characters from a data entry", "-" * 10)
printable = set(s.printable)
# \x00, \x02, \x10 are invisible control characters that corrupt data
badData = "Data with \x00funny \x02Characters is \x10bad!"
# Keep only characters that are in the printable set, then join them back into a string
cleanData = "".join(filter(lambda x: x in s.printable, badData))
print(f"Bad Data: <{badData}>")
print(f"Clean Data: <{cleanData}>")

# --- Cleaning 3: reformat a date into a required format ---
print(
    "-" * 10, "Reformatting data entry to match specific formatting criteria", "-" * 10
)
badData = dt.date(2026, 7, 23)
# Convert the date object to a string in YYYY-MM-DD format
badData = format(badData, "%Y-%m-%d")
# Parse the string back into a datetime object
cleanData = dt.datetime.strptime(badData, "%Y-%m-%d")
# Reformat it as "day full-month-name year", e.g. 23 July 2026
cleanData = format(cleanData, "%d %B %Y")
print(f"Bad Data: <{badData}>")
print(f"Clean Data: <{cleanData}>")
