from recommendation_engine import movies, recommend_movies

# Select a movie to test
selected_movie = movies[movies["title"] == "Inception"]

if selected_movie.empty:
    print("Movie not found.")
else:
    movie_id = int(selected_movie.iloc[0]["id"])

    print("Selected movie: Inception")
    print("\nRecommended movies:")

    recommendations = recommend_movies(movie_id)

    print(recommendations.to_string(index=False))