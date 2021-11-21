# Project Movie Recommendation


Creating a movie suggestion algorithm based on watch history.
=======
=======
## Overview of Analysis
Our movie recommendation engine creates a movie suggestion algorithm based on the user's watched history. When user inputs the movie title on the dashboard, it dynamically displays the metadata of the selected movie like the title, IMDB url, release year, average rating and tagged genres. On pressing the "Show Recommendation" button, it calls our flask app which invoked the K means ML model to bring a list of 5 recommendations for the input movie.




## Communication protocols
We have four members in our team. All the 4 members of this team had specific roles throughout the project. We used Slack, video chat and git commits to communicate the project progress internally. We meet every week to share the updates and discuss any issues we are facing.

## Project Outline
### Getting and Storing Data
Pull the data from https://datasets.imdbws.com/. Dataset Details can be viewed at https://www.imdb.com/interfaces/

### SQL Database
Create ERD Schema
Create tables to store movie data

![image](https://user-images.githubusercontent.com/85711507/142744836-c2c47d34-e8d5-4fe4-a7f3-19c904bbee47.png)


### Machine Learning Model
K-MEANS MACHINE and Hierarchical Learning model has been used for our training and testing setup.


### Dashboard
We have made an HTML based UI which takes the user input of movie titles and calls the flask app from the UI which will execute the K means model we are building to get the list of recommended movies which Flask app will return to render it on the UI.

### Presentation in Google Slides.


## Technologies used

<img width="640" alt="Technologies used" src="https://user-images.githubusercontent.com/85711507/142743488-353115cf-50e0-436e-846f-95f25575fed4.png">



## Data Exploration and preliminary analysis

0. Download data from https://datasets.imdbws.com/

- title.basics.tsv.gz (11/12/2021)
- title.akas.tsv.gz (11/12/2021)
- title.ratings.tsv.gz (11/11/2021)

    Dataset Details can be viewed at https://www.imdb.com/interfaces/


1. Unzip all three files to *.tsv

2. Rename title.basics.tsv to title_basics.tsv
    Since title_basics.tsv is 700 mb in its original form, filter entries on a Bash Terminal      prior to loading into Python using the following command, which filters entries only to Non-Adult Movie Titles with No NULLS
 ('endYear' column is dropped in process):



perl -F"\t" -lne 'print $F[0]."\t".$F[1]."\t".$F[2]."\t".$F[3]."\t".$F[4]."\t".$F[5]."\t".$F[7]."\t".$F[8]' title_basics.tsv | perl -F"\t" -lne 'print if $.==1 || ($_!~/\\N/ && $F[1]=~/movie/ && $F[4]=~/0/ && $F[7]!~/Adult/)' > title_basics_non-adult_movies_no_nulls.tsv



3. Rename title.akas.tsv to title_akas.tsv
    Obtain US-only Title IDs from title_akas.tsv using the following command on a Bash Terminal:

 awk -F"\t" 'NR==1 || $4~/US/{print $1}' title_akas.tsv | sort | uniq > US_title_ids.csv


4. Rename title.ratings.tsv to title_ratings.tsv
    Convert title_ratings.tsv to CSV via the following command on a Bash Terminal:
    
     cat title_ratings.tsv | tr "\t" "," > title_ratings.csv



5. Perform subsequent exploratory data analysis and data cleaning using Python     running within Jupyter Notebook.

- Remove Titles where primaryTitle is not the same as originalTitle in order to      filter out films which were US Releases of Foreign Films.

- In order to guarantee title uniqueness for remakes, search for duplicate primaryTitle and concatenate Film Release Year to the primaryTitle.

- Filter Titles for Title IDs that are only present in the  titles_us_ids_only list.

- Include Titles only released in 1920 or later.


## Database
We used the AWS RDS database to store the IMDB Movie Titles, their IDs and corresponding ratings in g_mvs_title_basics, g_mvs_us_little_ids and g_mvs_title_rating table respectively. As part of the training data preparation, we dropped the data where movies with primary title differs from the original title, or in case their IDs are missing or movie year is earlier than 1920. As part of the last step, we merged the movie title metadata with ratings data on the title ID and augment it with the IMDB title URL.

## Machine Learning Models

Once data preparation is done, we used the multi label bin analyzer to transform the converted genres lists. This transformed data frame ‘X’ is then merged with the prepared movies dataframe (as part of the data preparation step). We also merged the average rating in the transformed DF using primary title as a new index. 

Once above step is completed, we perform the Primary Component Analysis to reduce the dimensions with only three primary principal components and named them “PC 1”, “PC 2” and “PC 3”. As our final step, we performed the K means clustering using k=4 and fit the model. As a disclaimer, we also tried using the hierarchical model, but it being extremely resource intensive, was dropped in favor of the K means model. Once  K means model fits well, it is used to make the movie recommendation.

## Dashboard

![movies_recommendation_engine_goldfinger](https://user-images.githubusercontent.com/85711507/142745152-8562626d-e67b-42b2-84b3-ede8d7b560f9.png)


## Result of Analysis







## Recommendations for Future Analysis
For future analysis we would build a more robust algorithm




## What the Team would do differently

Initially we lost some time investigating the datasets. The original dataset we chose didn’t work as we expected. So we had to fetch fresh data from IMDB and as a result changes were made in the database. 
Also it would have been great to have more clarity on the roles and project course material. It took us a while to understand our roles and the project deliverables.








