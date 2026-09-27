import pandas as pd
import mysql.connector
from getpass import getpass

# 1. Read the cleaned CSV file
df = pd.read_csv("data/movies_cleaned.csv")

# 2. Convert missing values to None for MySQL
df = df.astype(object).where(pd.notna(df), None)

# 3. Convert release_date strings to Python date objects
df["release_date"] = pd.to_datetime(
    df["release_date"], errors="coerce"
).dt.date

# Replace invalid dates with None
df["release_date"] = df["release_date"].where(
    df["release_date"].notna(), None
)

# 4. Connect to MySQL
password = getpass("Enter your MySQL password: ")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="movie_recommender"
)

cursor = connection.cursor()

# 5. Prepare the SQL insert query
sql = """
INSERT INTO movies (
    id, title, genres, overview, release_date,
    rating, vote_count, release_year, description
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# 6. Convert the DataFrame into rows
rows = list(df.itertuples(index=False, name=None))

# 7. Insert all movie records
cursor.executemany(sql, rows)

# 8. Save the changes
connection.commit()

print(f"Successfully imported {cursor.rowcount} movies!")

# 9. Close the connection
cursor.close()
connection.close()