# Project Movie Recommendation
## Selected Topic

Tom2 Branch.

Creating a movie suggestion algorithm based on watch history.

## Reason for Selecting the topic
=======
Our project will be Movie suggestion based on watched history. 

## Reason for Selecting the topic

The purpose of this project is to get movie recommendation based on the watched history of user. 

## Description of Source Data
The source data will be the files movies_metadata.csv and ratings_small.csv.  These files are sourced from kaggle and imdb.  Watched_list.csv, 


## Description of Communication protocols
We will be using Slack, video chat and git commits for our project for the purpose of communication.
=======
The source data will be the three csv files Watched_list.csv, movies_metadata.csv, ratings_small.csv.

## Description of Communication protocols

We will be using Slack, video chat and git commits for our project for the purpose of communication.


## Technologies Used
### Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

### Database Storage
At the moment the intention is to store the SQL database locally.  If necessary AWS will be used to facilitate open access.

### Machine Learning
K-MEANS MACHINE Learning model will be used for our training and testing setup. Training dataset will be a file called watched_list.csv, which contains imdb and watched history data from one of the team members.

### Dashboard
We will make a HTML based UI which will take the user input of movie titles (user id from the ratings_small). Call the flask app from the UI which will execute the K means model we are building to get the list of recommended movies which Flask app will return to render it on the UI.
