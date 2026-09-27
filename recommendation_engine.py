import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load the cleaned movie dataset
movies = pd.read_csv("data/movies_cleaned.csv")

# 2. Replace missing descriptions with empty strings
movies["description"] = movies["description"].fillna("")

# 3. Convert descriptions into numerical vectors
vectorizer = TfidfVectorizer(stop_words="english")

tfidf_matrix = vectorizer.fit_transform(movies["description"])

# 4. Find recommendations for a selected movie
def recommend_movies(movie_id, number_of_recommendations=5):

    # Find the selected movie's position
    movie_positions = movies.index[movies["id"] == movie_id].tolist()

    if not movie_positions:
        return pd.DataFrame()

    movie_position = movie_positions[0]

    # Compare the selected movie with all other movies
    similarity_scores = cosine_similarity(
        tfidf_matrix[movie_position],
        tfidf_matrix
    ).flatten()

    # Sort movies by similarity, highest first
    similar_positions = similarity_scores.argsort()[::-1]

    # Remove the selected movie itself
    similar_positions = [
        position
        for position in similar_positions
        if position != movie_position
    ]

    # Get the top recommendations
    top_positions = similar_positions[:number_of_recommendations]

    recommendations = movies.iloc[top_positions].copy()

    recommendations["similarity_score"] = [
        round(float(similarity_scores[position]), 3)
        for position in top_positions
    ]

    return recommendations[
        ["id", "title", "genres", "release_year", "rating", "similarity_score"]
    ]