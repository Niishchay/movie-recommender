# Movie Recommender

A movie recommendation web app that uses a content-based filtering approach. The app loads cleaned movie data, stores it in MySQL, and recommends similar movies based on movie descriptions using TF-IDF and cosine similarity.

## Features

- Browse movies from the database
- Search for movies by title
- Click any movie to view similar recommendations
- Simple HTML/CSS/JavaScript frontend
- Flask API backend

## Tech Stack

- Python
- Flask
- MySQL
- Pandas
- scikit-learn
- HTML, CSS, JavaScript

## Project Structure

```text
movie-recommender/
├── app/
│   ├── __init__.py
│   ├── app.py
│   └── db.py
├── data/
│   ├── movies_cleaned.csv
│   └── tmdb_5000_movies.csv
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── .env.example
├── .gitignore
├── clean_data.py
├── import_movies.py
├── inspect_data.py
├── recommendation_engine.py
├── requirements.txt
├── test_db.py
├── test_recommendations.py
├── verify_data.py
├── README.md
└── .env
```

## Prerequisites

Before running the project, make sure you have:

- Python 3.9+
- MySQL Server installed and running
- A MySQL user with access to create and use a database

## 1) Clone or Download the Project

```bash
git clone <your-repository-url>
cd movie-recommender
```

## 2) Create a Virtual Environment

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3) Install Dependencies

```bash
pip install -r requirements.txt
```

## 4) Configure Database Settings

Create a file named `.env` in the project root using the sample below.

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=movie_recommender
```

You can copy from `.env.example` as a starting point.

> Do not upload your real `.env` file to GitHub or share it publicly because it contains your database password.

## 5) Create the MySQL Database and Table

Open MySQL and run:

```sql
CREATE DATABASE movie_recommender;
USE movie_recommender;

CREATE TABLE movies (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    genres VARCHAR(255),
    overview TEXT,
    release_date DATE,
    rating FLOAT,
    vote_count INT,
    release_year INT,
    description TEXT
);
```

## 6) Import Movie Data into MySQL

Run:

```bash
python import_movies.py
```

This script reads the cleaned CSV file from `data/movies_cleaned.csv` and inserts the movie records into the `movies` table.

## 7) Run the Flask API

From the project root:

```bash
python app/app.py
```

The backend runs at:

```text
http://127.0.0.1:5000
```

## 8) Run the Frontend

Open a second terminal and run:

```bash
cd frontend
python -m http.server 8000
```

Then open your browser at:

```text
http://localhost:8000
```

## API Endpoints

### Get all movies

```http
GET /api/movies
```

### Search movies

```http
GET /api/search?q=avatar
```

### Get recommendations for a movie

```http
GET /api/recommend/11
```

## Notes for Sharing the Project

When sending this project to someone else, share the project files, not the local environment.

### Share these items

- Entire source code folder
- `requirements.txt`
- `data/` folder with CSV data
- `README.md`
- `.env.example`

### Do not share

- `.venv/` folder
- `__pycache__/` folders
- local `.env` with real database credentials
- any local machine-specific settings

### Best practice

Use GitHub or a zip file containing the project source, then tell the other person to do the installation steps above and create their own `.env` file.

## Troubleshooting

### MySQL connection error

Check:

- MySQL is running
- `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` are correct
- the database exists
- the user has permission to access it

### No recommendations shown

Make sure:

- the database table is populated
- `python import_movies.py` ran successfully
- the Flask app is running

### Frontend cannot load data

Check that:

- the backend is running on port 5000
- the browser is loading the frontend from a local server
- CORS is enabled in `app/app.py`

## License

This project is for educational/demo purposes.
