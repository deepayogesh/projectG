# Project Movie Recommendation

## Overview of Analysis
Our movie recommendation engine creates a movie suggestion algorithm based on the user's choice of a movie they enjoyed. When user inputs the movie title on the dashboard, it dynamically displays the metadata of the selected movie like the title, IMDB url, release year, average rating and tagged genres. On pressing the "Get Recommendations" button, it calls our flask app which invokes the K means ML model to bring a list of 5 recommendations for the input movie.


## Communication protocols
We have four members in our team. All the 4 members of this team had specific roles throughout the project. We used Slack, video chat and git commits to communicate the project progress internally. We met every week to share the updates and discuss any issues we were facing.

## Project Outline
### Getting and Storing Data
Pull the data from https://datasets.imdbws.com/. Dataset Details can be viewed at https://www.imdb.com/interfaces/

### SQL Database
Create ERD Schema
Create tables to store movie data

![image](https://user-images.githubusercontent.com/85711507/142744836-c2c47d34-e8d5-4fe4-a7f3-19c904bbee47.png)


### Machine Learning Model
K-MEANS and Hierarchical clustering machine learning models were tested for clustering output.


### Dashboard
We have made an HTML based UI which takes the user input of movie title and calls the flask app from the UI which will execute the K means model we have build to get the list of recommended movies which Flask app will return to render it on the UI.

### Presentation in Google Slides.
https://docs.google.com/presentation/d/1tgqQFmfIOF4AMteqZtrhcAjbesh_rU_qWRb9vEfeG2g/edit?usp=sharing


## Technologies used

<img width="591" alt="Technologies used" src="https://user-images.githubusercontent.com/85711507/142773332-806a9c42-5809-4a4f-956b-d3bf2ee5b5c4.png">



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
We used the AWS RDS database to store the IMDB Movie Titles, their IDs and corresponding ratings in g_mvs_title_basics, g_mvs_us_little_ids and g_mvs_title_rating table respectively. As part of the data preparation, we dropped the data where movies with primary title differs from the original title, or in case their IDs are missing or movie year is earlier than 1920. As part of the last step, we merged the movie title metadata with ratings data on the title ID and augment it with the IMDB title URL.

## Machine Learning Models

Once data preparation is done, we used the multi label bin analyzer to transform the converted genres lists. This transformed data frame ‘X’ is then merged with the prepared movies dataframe (as part of the data preparation step). We also merged the average rating in the transformed DF using primary title as a new index. 

Once above step is completed, we perform the Primary Component Analysis to reduce the dimensions with only three primary principal components and named them “PC 1”, “PC 2” and “PC 3”. As our final step, we performed the K means clustering using k=4 and fit the model since we had previously determined that 4 was the ideal number for elbow curve. As a disclaimer, we also tried using the hierarchical model, but it being extremely resource intensive, was dropped in favor of the K means model. Once  K means model fits well, it is used to make the movie recommendation.

## Dashboard

Below is the screenshot of how our Dashboard looks like after we input movie title. When we input the movie title it provides the user with input movie information which includes the movie title, imdb url, release year, average rating and movie genres. Once user clicks the "Get recommendations" button, they will get five unique movie recommendations.

![movies_recommendation_engine_goldfinger](https://user-images.githubusercontent.com/85711507/142745152-8562626d-e67b-42b2-84b3-ede8d7b560f9.png)

## Result of Analysis

For most movies we input in the recommendation engine we get good recommendation from subjective point of view. For example when we input Toy Story and click on "Get recommendation" button the out put is all relevant movies which user would prefer to watch. We tested handful of random movies from many different genres and we subjectively analyzed the results and all of them appeared to be good recommendations.  

![movies_recommendation_engine_toy_story](https://user-images.githubusercontent.com/85711507/142952385-ba90f4c6-729e-4bc8-be37-43a75abfd738.png)


## Recommendations for Future Analysis
For future enhancements, we would build a more robust algorithm and also would apply genres as the output filter. This was a very challenging task and required more time to implement. More inputs based on individual ratings data can be applied in order to build a robust recommendation engine. A larger selection criteria can as well be implemented in order for user to provide with more options. Displaying the movie posters on the flask app would definitely make the recommendation engine look more appealing to the audience. All these recommendations would definitely help in building a better recommendation engine for user. 


## What the Team would do differently

Initially we lost some time investigating the datasets. The original dataset we chose didn’t work as we expected. So we had to fetch fresh data from IMDB and as a result changes were made in the database. 
Also it would have been great to have more clarity on the roles and project course material. It took us a while to understand our roles and the project deliverables.






