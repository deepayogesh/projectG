# Project Movie Review
## Selected Topic
Our team is creating a movie suggestion algorithm based on the user's recent film history and review scores.

## Reason for Selecting the topic


## Description of Source Data
Data will be sourced from kaggle, containing a common seperated list of films and their metadata.

## Technologies Used
### Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

### Database Storage
We will not host database on Amazon or any other place. We will be using csv files as the main source.

### Machine Learning
K-MEANS MACHINE Learning model will be used for our training and testing setup. Training dataset will be watched_list.csv.

### Dashboard
We will make a HTML based UI which will take the user input of user id (user id from the ratings_small). Call the flask app from the UI which will execute the K means model we are building to get the list of recommended movies which Flask app will return to render it on the UI.
