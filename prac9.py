import pandas as pd  # For loading the dataset
import matplotlib.pyplot as plt  # For creating the visualisations

# Load the fitness tracker data and display it
df = pd.read_csv("/home/user/mscit/ds/Fitness Tracker Data.csv")
print(df)

# Plot 1: Area plot of all numeric columns (stacked=False so areas overlap)
df.plot(kind="area", figsize=(10,5), stacked=False)
plt.title("Area Plot of Fitness Metrics")
plt.xlabel("Data Entry Index")
plt.ylabel("Metric Values")
plt.figure(figsize = (10,5))  # Start a new figure for the next plot

# Plot 2: Scatter plot to see if longer workouts burn more calories
plt.scatter(df["Duration_min"], df["Calories_Burned"])
plt.title("Workout Duration vs Calories Burned")
plt.xlabel("Duration(minutes)")
plt.ylabel("Calories Burned")
plt.figure(figsize = (10,5))

# Plot 3: Line chart of every metric across sessions
# Exclude the non-numeric/ID columns, which can't be plotted as lines
columns_to_plot = df.columns.drop(["UserID", "Day_of_Week", "Activity"])
x_data = range(0, df.shape[0])  # Session numbers 0, 1, 2, ... for the x-axis
for column in columns_to_plot:
    plt.plot(x_data, df[column], label=column)

plt.title("Trend of Fitness Metrics")
plt.xlabel("Workout Session Index")
plt.ylabel("Value")

plt.legend()
plt.figure(figsize= (10,5))
# Plot 4: Histogram showing how often each activity type occurs
plt.hist(df["Activity"])
plt.title("Frequency of Different Activities")
plt.xlabel("Activity Type")
plt.ylabel("Frequency (Number of Sessions)")
plt.figure(figsize= (10,5))
# Plot 5: Bar chart of calories burned for each day of the week
plt.bar(df["Day_of_Week"], df["Calories_Burned"])
plt.title("Calories Burned by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Calories Burned")
plt.tight_layout()  # Adjust spacing so labels don't overlap
plt.show()  # Display all the figures
