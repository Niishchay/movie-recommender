
const API_BASE_URL = "http://127.0.0.1:5000/api";

// Load movies when the page opens
document.addEventListener("DOMContentLoaded", () => {
    loadMovies();
});

// Fetch movies from the Flask API
async function loadMovies() {
    const container = document.getElementById("moviesContainer");

    container.innerHTML = '<p class="message">Loading movies...</p>';

    try {
        const response = await fetch(`${API_BASE_URL}/movies`);

        if (!response.ok) {
            throw new Error("Failed to fetch movies");
        }

        const movies = await response.json();

        displayMovies(movies);
    } catch (error) {
        console.error("Error loading movies:", error);
        container.innerHTML =
            '<p class="message">Unable to load movies. Make sure Flask is running.</p>';
    }
}

// Display movies as cards
function displayMovies(movies) {
    const container = document.getElementById("moviesContainer");

    container.innerHTML = "";

    if (movies.length === 0) {
        container.innerHTML = '<p class="message">No movies found.</p>';
        return;
    }

    movies.forEach((movie) => {
        const card = document.createElement("div");
        card.className = "movie-card";

        const year = movie.release_year || "Year unavailable";
        const rating = movie.rating ?? "Not rated";

        card.innerHTML = `
            <div class="movie-info">
                <h3>${movie.title}</h3>
                <p>${movie.genres || "Genre unavailable"}</p>
                <p>Year: ${year}</p>
                <p>Rating: ${rating}</p>
            </div>
        `;

        // Make the movie card clickable
        card.style.cursor = "pointer";

        card.addEventListener("click", () => {
            loadRecommendations(movie.id, movie.title);
        });

        container.appendChild(card);
    });
}

// Search movies when the Search button is clicked
document.getElementById("searchButton").addEventListener("click", searchMovies);

// Also search when Enter is pressed
document.getElementById("searchInput").addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        searchMovies();
    }
});

async function searchMovies() {
    const searchInput = document.getElementById("searchInput");
    const query = searchInput.value.trim();

    const container = document.getElementById("moviesContainer");

    if (!query) {
        loadMovies();
        return;
    }

    container.innerHTML = '<p class="message">Searching movies...</p>';

    try {
        const response = await fetch(
            `${API_BASE_URL}/search?q=${encodeURIComponent(query)}`
        );

        if (!response.ok) {
            throw new Error("Search failed");
        }

        const movies = await response.json();
        displayMovies(movies);
    } catch (error) {
        console.error("Error searching movies:", error);
        container.innerHTML =
            '<p class="message">Unable to search movies. Please try again.</p>';
    }
}

async function loadRecommendations(movieId, movieTitle) {
    const container = document.getElementById("recommendationsContainer");

    container.innerHTML = `
        <h2>Movies similar to ${movieTitle}</h2>
        <p class="message">Finding recommendations...</p>
    `;

    try {
        const response = await fetch(
            `${API_BASE_URL}/recommend/${movieId}`
        );

        if (!response.ok) {
            throw new Error("Failed to fetch recommendations");
        }

        const movies = await response.json();

        container.innerHTML = `
            <h2>Movies similar to ${movieTitle}</h2>
        `;

        if (movies.length === 0) {
            container.innerHTML +=
                '<p class="message">No recommendations found.</p>';
            return;
        }

        movies.forEach((movie) => {
            const card = document.createElement("div");
            card.className = "movie-card";

            card.innerHTML = `
                <div class="movie-info">
                    <h3>${movie.title}</h3>
                    <p>${movie.genres || "Genre unavailable"}</p>
                    <p>Year: ${movie.release_year || "Unavailable"}</p>
                    <p>Rating: ${movie.rating ?? "Not rated"}</p>
                </div>
            `;

            container.appendChild(card);
        });

    } catch (error) {
        console.error("Error loading recommendations:", error);

        container.innerHTML = `
            <h2>Movies similar to ${movieTitle}</h2>
            <p class="message">
                Unable to load recommendations. Please try again.
            </p>
        `;
    }
}