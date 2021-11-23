from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
movies = []


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Search Movies
@app.route("/movies", methods=["GET"])
def search_movies():
    searchTerm = request.args.get('term')
    take = 20

    # Filters the movies based on search term and then takes from the top
    # Definitely not the most efficient but good enough
    # There are better data models for searching list of strings
    filtered_movies = [movie for movie in movies if searchTerm in movie]
    top_filtered_movies = filtered_movies[:take]

    return jsonify(top_filtered_movies)

# Handle startup tasks
def startup():
    # Load all the movies from ./data/movies.txt
    global movies
    with open("./Desktop/Class Data/FinalProject/autocomplete-flask/data/movies.txt") as file:
        movies = [line.strip() for line in file.readlines()] # strip takes off all the newline characters
    movies.sort()
    
    # Run the app
    app.run(debug=True)


if __name__ == '__main__':
    startup()
