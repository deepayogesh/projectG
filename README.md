# Project Movie Recommendation
## Selected Topic
Our project will be Movie suggestion based on watched history. 

## Reason for Selecting the topic

The purpose of this project is to get movie recommendation based on the watched history of user. 

## Description of Source Data

The source data will be the three csv files Watched_list.csv, movies_metadata.csv, ratings_small.csv.

## Description of Communication protocols

We will be using Slack, video chat and git commits for our project for the purpose of communication.


## Technologies Used
### Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

### Database Storage
We will not host database on Amazon or any other place. We will be using csv files as the main source.

### Machine Learning
K-MEANS MACHINE Learning model will be used for our training and testing setup. Training dataset will be watched_list.csv.

### Dashboard
We will make a HTML based UI which will take the user input of movie titles (user id from the ratings_small). Call the flask app from the UI which will execute the K means model we are building to get the list of recommended movies which Flask app will return to render it on the UI.
