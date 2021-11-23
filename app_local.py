# Import Dependencies
from flask import Flask, render_template, redirect, url_for, request
import model_local


#################################################
# START Flask Setup
#################################################

app = Flask(__name__)

# Define Flask Routes

# Main Index Page

@app.route("/", methods=['GET', 'POST'])

def index():
    movie = ""
    errors = []
    recommendations = []
    input_title_info = {}


    if request.method == "POST":
        try:
            # Get Input Movie from User
            movie = request.form['inputMovie']

            # Get List of Available Titles from Source Data
            available_titles = model_local.get_titles()

            if (movie in available_titles):
                input_title_info = model_local.get_inputTitle_info(movie)
                recommendations = model_local.get_movies(movie)
            else:
                movie = movie + " - Title Not Found"

        except:
            errors.append(
                    "Unable to find Movie. Please try again."
                    )


    return render_template("index_local.html", errors=errors, movie=movie, input_title_info=input_title_info, recommendations=recommendations)


#################################################
# END Flask Setup
#################################################

# main behavior
if __name__ == "__main__":
   #app.run()
   app.run(debug=True)
