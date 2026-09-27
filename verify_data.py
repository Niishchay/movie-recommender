import pandas as pd

df = pd.read_csv("data/movies_cleaned.csv", keep_default_na=False)

print("--- Dataset Shape ---")
print(df.shape)

print("\n--- Columns ---")
print(df.columns.tolist())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate IDs ---")
print(df["id"].duplicated().sum())

print("\n--- Missing Descriptions ---")
print(df["description"].isnull().sum())

print("\n--- Sample Movies ---")
print(df[["title", "genres", "release_year", "rating"]].head())

print("Empty genres:", df["genres"].str.strip().eq("").sum())
print("Empty overviews:", df["overview"].str.strip().eq("").sum())
print("Empty descriptions:", df["description"].str.strip().eq("").sum())