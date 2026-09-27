import pandas as pd

# Load the movie dataset
df = pd.read_csv("data/tmdb_5000_movies.csv")

# Display the first 5 rows
print("\n--- First 5 Movies ---")
print(df.head())

# Display the dataset dimensions
print("\n--- Dataset Shape ---")
print(df.shape)

# Display column names
print("\n--- Column Names ---")
print(df.columns.tolist())

# Display data types and non-null counts
print("\n--- Dataset Information ---")
df.info()

# Count missing values in each column
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Count duplicate rows
print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

# Check for duplicate movie IDs
print("\n--- Duplicate Movie IDs ---")
print(df["id"].duplicated().sum())

# Check for missing movie titles
print("\n--- Missing Titles ---")
print(df["title"].isnull().sum())

# Check for empty movie descriptions
print("\n--- Empty Overviews ---")
print(df["overview"].fillna("").str.strip().eq("").sum())