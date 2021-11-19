# Import Dependencies
from flask import Flask, render_template, redirect, url_for, request
import numpy as np
import re
from sqlalchemy import create_engine
import psycopg2
from config import db_password
import time
import model


#################################################
# START Flask Setup
#################################################

app = Flask(__name__)

# Define Flask Routes

@app.route("/", methods=['GET', 'POST'])

def index():
    movie = ""
    errors = []
    recommendations = []
    input_title_info = {}


    if request.method == "POST":
        try:
            movie = request.form['inputMovie']
            #recommendations.append(movie)
            input_title_info = model.get_inputTitle_info(movie)
            recommendations = model.get_movies(movie)

        except:
            errors.append(
                    "Unable to find Movie. Please try again."
                    )


    return render_template("index.html", errors=errors, movie=movie, input_title_info=input_title_info, recommendations=recommendations)

#@app.route("/testDBConnection")

#def testDBConnection():  
    # Connect data to SQL - postgreSQL
#    db_string = f'postgresql://postgres:{db_password}@127.0.0.1:5432/MoviesRecommendationDB'
#    engine=create_engine(db_string)
#    print(engine)
#    return redirect('/', code=302)

# Route to Generate Recommendations
#@app.route("/recommendations")

#def get_recommendations():
    #movies = ["The Third Man", "The African Queen", "Charade", "Casablanca", "Jurassic Park"]

    #return movies
    #return redirect("/", code=302)

#################################################
# END Flask Setup
#################################################

# main behavior
if __name__ == "__main__":
   #app.run()
   app.run(debug=True)
