from flask import Flask, jsonify, request
from flask_cors import CORS
from app.db import get_db_connection
from recommendation_engine import recommend_movies

app = Flask(__name__)

CORS(app)

@app.route("/api/recommend/<int:movie_id>", methods=["GET"])
def get_recommendations(movie_id):

    recommendations = recommend_movies(movie_id)

    if recommendations.empty:
        return jsonify({"error": "Movie not found."}), 404

    # Convert the recommendation results into JSON-safe Python data
    result = recommendations.to_json(orient="records")

    import json
    return jsonify(json.loads(result))

@app.route("/api/search", methods=["GET"])
def search_movies():

    search_query = request.args.get("q", "").strip()

    if not search_query:
        return jsonify({"error": "Please provide a search query."}), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT id, title, genres, release_year, rating
            FROM movies
            WHERE title LIKE %s
            ORDER BY title
            LIMIT 20
        """

        cursor.execute(query, (f"%{search_query}%",))
        movies = cursor.fetchall()

        return jsonify(movies)

    finally:
        cursor.close()
        connection.close()


@app.route("/api/movies", methods=["GET"])
def get_movies():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT id, title, genres, release_year, rating
            FROM movies
            ORDER BY title
            LIMIT 100
        """

        cursor.execute(query)
        movies = cursor.fetchall()

        return jsonify(movies)

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    app.run(debug=True)