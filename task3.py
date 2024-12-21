from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Sample data: Users and their preferences (movies)
data = {
    "User1": ["Inception", "Interstellar", "The Matrix"],
    "User2": ["The Matrix", "The Godfather", "The Dark Knight"],
    "User3": ["Inception", "The Dark Knight", "Avengers"],
    "User4": ["Interstellar", "Inception", "The Social Network"],
    "User5": ["Avengers", "The Social Network", "The Godfather"],
    "User6": ["The Dark Knight", "Inception", "The Matrix"]
}

# Movie descriptions for content-based filtering
movie_descriptions = {
    "Inception": "A sci-fi movie about dreams within dreams.",
    "Interstellar": "A journey to save humanity through space travel.",
    "The Matrix": "A hacker discovers the truth about reality.",
    "The Godfather": "A crime saga about a mafia family.",
    "The Dark Knight": "A superhero fights crime in Gotham City.",
    "Avengers": "Superheroes team up to save the world.",
    "The Social Network": "The story behind Facebook's creation.",
    "Titanic": "A romantic story set during the ill-fated voyage of the Titanic.",
    "Jurassic Park": "Dinosaurs are brought back to life in a theme park."
}

# List of all movies
all_movies = list(movie_descriptions.keys())

# Home route with search box
@app.route("/", methods=["GET", "POST"])
def home():
    search_term = request.args.get("search_term", "")
    search_results = search_movies(search_term)
    
    return render_template_string("""
        <html>
            <head>
                <style>
                    body {
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        text-align: center;
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        height: 100vh;
                        background-color: #f0f8ff; /* Light blue background */
                    }
                    form {
                        margin-bottom: 20px;
                    }
                    ul {
                        list-style-type: none;
                        padding: 0;
                    }
                    h1 {
                        color: #333; /* Darker text color for contrast */
                    }
                    input, button {
                        padding: 10px;
                        margin: 5px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                    }
                    button {
                        background-color: #007bff;
                        color: white;
                        border: none;
                        cursor: pointer;
                    }
                    button:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <h1>Movie Recommendation System</h1>
                <form action="/" method="get">
                    <input type="text" name="search_term" value="{{ search_term }}" placeholder="Search movies...">
                    <button type="submit">Search</button>
                </form>
                
                {% if search_term %}
                    <h2>Search Results for "{{ search_term }}":</h2>
                    {% if search_results %}
                        <ul>
                            {% for movie, description in search_results %}
                                <li><strong>{{ movie }}:</strong> {{ description }}</li>
                            {% endfor %}
                        </ul>
                    {% else %}
                        <p>No movies found.</p>
                    {% endif %}
                {% endif %}
            </body>
        </html>
    """, search_term=search_term, search_results=search_results)

# Search movies based on the term
def search_movies(search_term):
    if not search_term:
        return []

    # Simple search, case-insensitive
    return [(movie, movie_descriptions[movie]) for movie in all_movies if search_term.lower() in movie.lower()]

# Recommendation Route
@app.route("/recommend", methods=["GET"])
def recommend():
    user = request.args.get("user")
    if not user:
        return jsonify({"error": "User parameter is missing!"}), 400

    method = request.args.get("method", "content")
    if method not in ["content", "collaborative"]:
        return jsonify({"error": "Invalid method parameter! Use 'content' or 'collaborative'."}), 400

    top_n = int(request.args.get("top_n", 3))  # Default is 3 if not specified

    # Recommendation logic
    if method == "content":
        recommendations = content_based_recommendation(user, top_n)
    else:
        recommendations = collaborative_filtering_recommendation(user, top_n)

    return jsonify({"user": user, "method": method, "recommendations": recommendations})

# Content-based recommendation function
def content_based_recommendation(user, top_n=3):
    user_movies = data[user]
    user_movie_descriptions = [movie_descriptions[movie] for movie in user_movies]

    # Combine user movie descriptions into a single text
    user_profile = " ".join(user_movie_descriptions)

    # Create a TF-IDF matrix for all movies
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([user_profile] + [movie_descriptions[movie] for movie in all_movies])

    # Calculate cosine similarity between user profile and all movies
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Get top N recommendations excluding movies already watched
    recommendations = [(all_movies[i], similarity_scores[i]) for i in range(len(all_movies)) if all_movies[i] not in user_movies]
    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
    return [movie for movie, score in recommendations[:top_n]]

# Collaborative filtering recommendation function
def collaborative_filtering_recommendation(user, top_n=3):
    user_movies = set(data[user])
    other_users = {u: set(movies) for u, movies in data.items() if u != user}

    # Find movies liked by similar users
    similar_movies = {}
    for other_user, movies in other_users.items():
        similarity = len(user_movies & movies) / len(user_movies | movies)
        for movie in movies - user_movies:
            if movie not in similar_movies:
                similar_movies[movie] = 0
            similar_movies[movie] += similarity

    # Sort by similarity score
    sorted_movies = sorted(similar_movies.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, score in sorted_movies[:top_n]]

if __name__ == "__main__":
    app.run(debug=True)
