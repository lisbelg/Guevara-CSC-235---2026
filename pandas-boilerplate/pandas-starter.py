# Import pandas library
import pandas as pd

# Load CSV file into DataFrame
data = pd.read_csv("sample-data.csv")

# Display first 5 rows
print("First 5 Rows:")
print(data.head())

# Show summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Show column names
print("\nColumn Names:")
print(data.columns)