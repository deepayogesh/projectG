# Import Dependencies
from flask import Flask, render_template, redirect, url_for, request
import model


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
            movie = request.form['inputMovie']
            input_title_info = model.get_inputTitle_info(movie)
            recommendations = model.get_movies(movie)

        except:
            errors.append(
                    "Unable to find Movie. Please try again."
                    )


    return render_template("index.html", errors=errors, movie=movie, input_title_info=input_title_info, recommendations=recommendations)


#################################################
# END Flask Setup
#################################################

# main behavior
if __name__ == "__main__":
   #app.run()
   app.run(debug=True)
