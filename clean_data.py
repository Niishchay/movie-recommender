import pandas as pd
import json

# Load the original dataset
df = pd.read_csv("data/tmdb_5000_movies.csv")

# Keep only the columns needed for our project
df = df[
    ["id", "title", "genres", "overview",
     "release_date", "vote_average", "vote_count"]
].copy()

# Remove rows with missing or blank titles
df = df.dropna(subset=["title"])
df = df[df["title"].str.strip() != ""]

# Remove duplicate movie IDs
df = df.drop_duplicates(subset=["id"])

# Clean movie titles
df["title"] = df["title"].str.strip()

# Replace missing descriptions with empty strings
df["overview"] = df["overview"].fillna("").str.strip()

# Extract genre names from JSON-like text
def extract_genres(value):
    try:
        genres = json.loads(value)
        return " ".join(
            genre["name"] for genre in genres
        )
    except (json.JSONDecodeError, TypeError):
        return ""

df["genres"] = df["genres"].apply(extract_genres)

# Convert release dates to datetime
df["release_date"] = pd.to_datetime(
    df["release_date"], errors="coerce"
)

# Extract release year
df["release_year"] = df["release_date"].dt.year

# Rename rating column
df = df.rename(columns={"vote_average": "rating"})

# Create combined text for recommendations
df["description"] = (
    df["genres"] + " " + df["overview"]
).str.strip()

# Remove movies without a release year
df = df.dropna(subset=["release_year"])

# Convert release year to integer
df["release_year"] = df["release_year"].astype(int)

# Save cleaned dataset
df.to_csv("data/movies_cleaned.csv", index=False)

print("Cleaning completed!")
print("Final dataset shape:", df.shape)
print(df.head())