#!/usr/bin/env python
# coding: utf-8

# ## Part 0: Import Dependencies and Set-Up

# Import Dependencies
#import config
import numpy as np
import os
import pandas as pd
#import psycopg2
import random
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, MultiLabelBinarizer, StandardScaler
import time


def get_titles():

    # Configure AWS RDS Connection:

    #engine = psycopg2.connect (
    #        database=config.db_database,
    #        user=config.db_user,
    #        password=config.db_password,
    #        host=config.db_host,
    #        port=config.db_port
    #        )

    # Path to file directory and variables for input files.
    file_dir = os.path.join("Data")

    # imdb Titles metadata (Extracted from title.basics.tsv)
    titles_metadata_file = f'{file_dir}/title_basics_non-adult_movies_no_nulls.tsv'

    # imdb US Titles only ids (Extracted from title.akas.tsv)
    titles_us_ids_only_file = f'{file_dir}/US_title_ids_unique.csv'

    # imdb Ratings data (Derived from title.ratings.tsv)
    ratings_data_file = f'{file_dir}/title_ratings.csv'



    # ## Part 1: Import Data, Clean and Transform Data

    # Import imdb Titles metadata, imdb US Title IDs, imdb Ratings data
    # From Local CSV

    titles_metadata = pd.read_csv(titles_metadata_file, sep='\t')
    titles_us_ids_only = pd.read_csv(titles_us_ids_only_file)
    ratings_data = pd.read_csv(ratings_data_file)

    # Import imdb Titles metadata, imdb US Title IDs, imdb Ratings data
    # From AWS RDS

    #import_query = "SELECT * FROM g_mvs_title_basics"
    #titles_metadata = pd.read_sql(import_query, engine)

    #import_query = "SELECT * FROM g_mvs_us_title_ids"
    #titles_us_ids_only = pd.read_sql(import_query, engine)

    #import_query = "SELECT * FROM g_mvs_title_ratings"
    #ratings_data = pd.read_sql(import_query, engine)


    # Close AWS RDS Connection:
    #engine.close()


    # Drop all Titles where primaryTitle differs from originalTitle
    # (Since language of titles is not often available, this is an attempt
    # to filter out obscure non-English language films)

    titles_metadata = titles_metadata.loc[titles_metadata['primaryTitle'] == titles_metadata['originalTitle']]


    # Look for Films with the same primaryTitle
    # and set primaryTitle to primaryTitle + (startYear)

    duplicate_titles_df = pd.concat(g for _, g in titles_metadata.groupby('primaryTitle') if len(g) > 1)

    duplicate_titles_df['primaryTitle'] = duplicate_titles_df.apply(lambda row: "".join([row['primaryTitle'], " (", str(row['startYear']), ")"]), axis=1)
    duplicate_titles_df['originalTitle'] = duplicate_titles_df['primaryTitle']


    # Merge duplicate_titles_df back with titles_metadata

    cols = list(titles_metadata.columns)
    titles_metadata.loc[titles_metadata['tconst'].isin(duplicate_titles_df['tconst']), cols] = duplicate_titles_df[cols]


    # Drop all Titles from titles_metadata that are not in titles_us_ids_only

    titles_metadata = pd.merge(titles_metadata, titles_us_ids_only, on='tconst', how='inner')
    titles_metadata = titles_metadata.drop_duplicates()


    # Convert startYear Column to int

    titles_metadata['startYear'] = pd.to_numeric(titles_metadata['startYear'])


    # Drop titles_metadata Rows with 'startYear' less than 1920

    titles_metadata = titles_metadata.loc[titles_metadata['startYear'] >= 1920]


    titles_list = titles_metadata['primaryTitle'].tolist()


    # Sort titles_list Alphabetically in Ascending Order

    titles_list.sort(reverse=False)


    return titles_list


def get_inputTitle_info(inputTitle):

    viewerTitle = inputTitle

    # Configure AWS RDS Connection:

    #engine = psycopg2.connect (
    #        database=config.db_database,
    #        user=config.db_user,
    #        password=config.db_password,
    #        host=config.db_host,
    #        port=config.db_port
    #        )

    # Path to file directory and variables for input files.
    file_dir = os.path.join("Data")

    # imdb Titles metadata (Extracted from title.basics.tsv)
    titles_metadata_file = f'{file_dir}/title_basics_non-adult_movies_no_nulls.tsv'

    # imdb US Titles only ids (Extracted from title.akas.tsv)
    titles_us_ids_only_file = f'{file_dir}/US_title_ids_unique.csv'

    # imdb Ratings data (Derived from title.ratings.tsv)
    ratings_data_file = f'{file_dir}/title_ratings.csv'



    # ## Part 1: Import Data, Clean and Transform Data

    # Import imdb Titles metadata, imdb US Title IDs, imdb Ratings data
    # From Local CSV

    titles_metadata = pd.read_csv(titles_metadata_file, sep='\t')
    titles_us_ids_only = pd.read_csv(titles_us_ids_only_file)
    ratings_data = pd.read_csv(ratings_data_file)

    # Import imdb Titles metadata, imdb US Title IDs, imdb Ratings data
    # From AWS RDS

    #import_query = "SELECT * FROM g_mvs_title_basics"
    #titles_metadata = pd.read_sql(import_query, engine)

    #import_query = "SELECT * FROM g_mvs_us_title_ids"
    #titles_us_ids_only = pd.read_sql(import_query, engine)

    #import_query = "SELECT * FROM g_mvs_title_ratings"
    #ratings_data = pd.read_sql(import_query, engine)

    # Close AWS RDS Connection:
    #engine.close()

    # Drop all Titles where primaryTitle differs from originalTitle
    # (Since language of titles is not often available, this is an attempt
    # to filter out obscure non-English language films)

    titles_metadata = titles_metadata.loc[titles_metadata['primaryTitle'] == titles_metadata['originalTitle']]


    # Look for Films with the same primaryTitle
    # and set primaryTitle to primaryTitle + (startYear)

    duplicate_titles_df = pd.concat(g for _, g in titles_metadata.groupby('primaryTitle') if len(g) > 1)

    duplicate_titles_df['primaryTitle'] = duplicate_titles_df.apply(lambda row: "".join([row['primaryTitle'], " (", str(row['startYear']), ")"]), axis=1)
    duplicate_titles_df['originalTitle'] = duplicate_titles_df['primaryTitle']


    # Merge duplicate_titles_df back with titles_metadata

    cols = list(titles_metadata.columns)
    titles_metadata.loc[titles_metadata['tconst'].isin(duplicate_titles_df['tconst']), cols] = duplicate_titles_df[cols]


    # Drop all Titles from titles_metadata that are not in titles_us_ids_only

    titles_metadata = pd.merge(titles_metadata, titles_us_ids_only, on='tconst', how='inner')
    titles_metadata = titles_metadata.drop_duplicates()


    # Drop titles_metadata Rows with "\N" for genres and startYear
    # Drop titleType isAdult and endYear Columns
    # Note: If using title_basics_non-adult_movies_no_nulls.tsv, 'endYear' and "\N" has already been removed.

    #titles_metadata = titles_metadata.loc[~(titles_metadata['genres'] == "\\N") & ~(titles_metadata['startyear'] == "\\N")]
    #titles_metadata.drop(['titleType'], axis=1, inplace=True)
    #titles_metadata.drop(['isAdult'], axis=1, inplace=True)
    #titles_metadata.drop(['endYear'], axis=1, inplace=True)


    # Convert startYear Column to int

    titles_metadata['startYear'] = pd.to_numeric(titles_metadata['startYear'])


    # Drop titles_metadata Rows with 'startYear' less than 1920

    titles_metadata = titles_metadata.loc[titles_metadata['startYear'] >= 1920]


    # Merge titles_metadata and ratings_data on tconst

    movies_df = pd.merge(titles_metadata, ratings_data, on="tconst")


    # Add url column to movies_df
    movies_df['url'] = movies_df.apply(lambda row: "".join(["https://www.imdb.com/title/", row['tconst'], "/"]), axis=1)

    # Find Records for inputTitle in movies_df

    inputTitle_info_dict = {}

    inputTitle_info_dict['url'] = movies_df.loc[movies_df['primaryTitle'] == inputTitle]['url'].values[0]
    inputTitle_info_dict['releaseYear'] = movies_df.loc[movies_df['primaryTitle'] == inputTitle]['startYear'].values[0]
    inputTitle_info_dict['averageRating'] = movies_df.loc[movies_df['primaryTitle'] == inputTitle]['averageRating'].values[0]
    inputTitle_info_dict['genres'] = movies_df.loc[movies_df['primaryTitle'] == inputTitle]['genres'].values[0].replace(",", ", ")

    return inputTitle_info_dict


def get_movies(inputTitle):

    start_time = time.time()

    viewerTitle = inputTitle

    # Configure AWS RDS Connection:

    #engine = psycopg2.connect (
    #        database=config.db_database,
    #        user=config.db_user,
    #        password=config.db_password,
    #        host=config.db_host,
    #        port=config.db_port
    #        )

    # Path to file directory and variables for input files.
    file_dir = os.path.join("Data")

    # imdb Titles metadata (Extracted from title.basics.tsv)
    titles_metadata_file = f'{file_dir}/title_basics_non-adult_movies_no_nulls.tsv'

    # imdb US Titles only ids (Extracted from title.akas.tsv)
    titles_us_ids_only_file = f'{file_dir}/US_title_ids_unique.csv'

    # imdb Ratings data (Derived from title.ratings.tsv)
    ratings_data_file = f'{file_dir}/title_ratings.csv'



    # ## Part 1: Import Data, Clean and Transform Data

    # Import imdb Titles metadata, imdb US Title IDs, imdb Ratings data
    # From Local CSV

    titles_metadata = pd.read_csv(titles_metadata_file, sep='\t')
    titles_us_ids_only = pd.read_csv(titles_us_ids_only_file)
    ratings_data = pd.read_csv(ratings_data_file)

    # Import imdb Titles metadata, imdb US Title IDs, imdb Ratings data
    # From AWS RDS

    #import_query = "SELECT * FROM g_mvs_title_basics"
    #titles_metadata = pd.read_sql(import_query, engine)

    #import_query = "SELECT * FROM g_mvs_us_title_ids"
    #titles_us_ids_only = pd.read_sql(import_query, engine)

    #import_query = "SELECT * FROM g_mvs_title_ratings"
    #ratings_data = pd.read_sql(import_query, engine)

    # Close AWS RDS Connection:
    #engine.close()

    # Drop all Titles where primaryTitle differs from originalTitle
    # (Since language of titles is not often available, this is an attempt
    # to filter out obscure non-English language films)

    titles_metadata = titles_metadata.loc[titles_metadata['primaryTitle'] == titles_metadata['originalTitle']]


    # Look for Films with the same primaryTitle
    # and set primaryTitle to primaryTitle + (startYear)

    duplicate_titles_df = pd.concat(g for _, g in titles_metadata.groupby('primaryTitle') if len(g) > 1)

    duplicate_titles_df['primaryTitle'] = duplicate_titles_df.apply(lambda row: "".join([row['primaryTitle'], " (", str(row['startYear']), ")"]), axis=1)
    duplicate_titles_df['originalTitle'] = duplicate_titles_df['primaryTitle']


    # Merge duplicate_titles_df back with titles_metadata

    cols = list(titles_metadata.columns)
    titles_metadata.loc[titles_metadata['tconst'].isin(duplicate_titles_df['tconst']), cols] = duplicate_titles_df[cols]


    # Drop all Titles from titles_metadata that are not in titles_us_ids_only

    titles_metadata = pd.merge(titles_metadata, titles_us_ids_only, on='tconst', how='inner')
    titles_metadata = titles_metadata.drop_duplicates()


    # Drop titles_metadata Rows with "\N" for genres and startYear
    # Drop titleType isAdult and endYear Columns
    # Note: If using title_basics_non-adult_movies_no_nulls.tsv, 'endYear' and "\N" has already been removed.

    #titles_metadata = titles_metadata.loc[~(titles_metadata['genres'] == "\\N") & ~(titles_metadata['startyear'] == "\\N")]
    #titles_metadata.drop(['titleType'], axis=1, inplace=True)
    #titles_metadata.drop(['isAdult'], axis=1, inplace=True)
    #titles_metadata.drop(['endYear'], axis=1, inplace=True)


    # Convert startYear Column to int

    titles_metadata['startYear'] = pd.to_numeric(titles_metadata['startYear'])


    # Drop titles_metadata Rows with 'startYear' less than 1920

    titles_metadata = titles_metadata.loc[titles_metadata['startYear'] >= 1920]


    # Merge titles_metadata and ratings_data on tconst

    movies_df = pd.merge(titles_metadata, ratings_data, on="tconst")


    # Add url column to movies_df
    movies_df['url'] = movies_df.apply(lambda row: "".join(["https://www.imdb.com/title/", row['tconst'], "/"]), axis=1)

    # Convert 'genres' entries into lists

    movies_df['genres_list'] = movies_df.apply(lambda row: row['genres'].split(","), axis=1)


    # Transform (get_dummies via Multi Label Bin Encoding) movies_df by 'genres'

    genres = movies_df['genres_list']

    mlb = MultiLabelBinarizer()

    X = pd.DataFrame(mlb.fit_transform(genres), columns=mlb.classes_, index=movies_df.index)

    # Merge X back with movies_df

    movies_df = pd.merge(movies_df, X, how='inner', left_index=True, right_index=True)


    # Integrate 'averageRating' into X DataFrame with 'primaryTitle' as new Index
    Z = pd.merge(movies_df[['primaryTitle', 'averageRating']], X, how='outer', left_index=True, right_index=True)
    Z.set_index('primaryTitle', inplace=True)


    # Standardize the data with StandardScaler()

    Z = StandardScaler().fit_transform(Z)


    # ## Part 2: Principal Component Analysis


    # Use PCA to reduce dimensions to three principal components
    pca = PCA(n_components=3)

    movies_pca = pca.fit_transform(Z)


    # Create a DataFrame with the three principal components
    col_names = ["PC 1", "PC 2", "PC 3"]
    movies_pca_df = pd.DataFrame(movies_pca, columns=col_names, index=movies_df.index)


    # ## Part 3: Clustering Using K-Means


    # Initialize the K-Means model using k=4

    model = KMeans(n_clusters=4, random_state=0)


    # Fit the model

    model.fit(movies_pca_df)



    # Predict clusters
    predictions = model.predict(movies_pca_df)


    # Create a new DataFrame including predicted clusters and movies metadata.
    # Concatenate the movies_df and movies_pca_df on the same columns.

    clustered_df = pd.concat([movies_df, movies_pca_df], axis=1, sort=False)


    # Add a new column, "Class" to the clustered_df DataFrame that holds the predictions.
    clustered_df['Class'] = model.labels_


    # ## Part 4: Generate Recommendation for User

    # Find tconst for viewerTitle

    viewer_tconst = clustered_df.loc[(clustered_df['primaryTitle'] == viewerTitle)]['tconst']


    # #### Take viewerTitle and find Closest Neighbor


    # Find Class of viewerTitle

    viewerTitleClass = clustered_df.loc[clustered_df['primaryTitle'] == viewerTitle]['Class'].values[0]


    # Create a Distance Matrix by 'tconst'

    # First, create a DataFrame of only the three Principal Components
    # of Titles in the same Class as viewerTitle

    clustered_df = clustered_df.loc[clustered_df['Class'] == viewerTitleClass]

    distance_inputs_df = clustered_df[['tconst', 'PC 1', 'PC 2', 'PC 3']]
    distance_inputs_df.set_index('tconst', inplace=True)


    # Find Principal Component Coordinates
    # for viewer_tconst

    viewer_input_df = distance_inputs_df.loc[viewer_tconst]


    # Convert distance_inputs_df to Numpy Array

    distance_inputs = distance_inputs_df.to_numpy()

    viewer_input = viewer_input_df.to_numpy()


    # Calculate Euclidean Distances

    #distance_results = distance.cdist(viewer_input, distance_inputs, 'euclidean')
    distance_results = cdist(viewer_input, distance_inputs, 'euclidean')


    # #### Output Recommendations

    # Find the k Smallest Non-Zero Distance and their Positions
    # Change k to change the number of Recommendations output

    k = 5

    # Sort distance_results Array
    # and exclude Zeroes

    distance_results_sorted = np.sort(distance_results[0])
    distance_results_sorted = distance_results_sorted[np.nonzero(distance_results_sorted)]
    
    time_elapsed = round(time.time() - start_time, 1)

    print(f'\nInput Movie: {viewerTitle}\n')

    print(f'Model Execution Time: {time_elapsed} seconds\n')

    print(f'Number of entries in Distance Array: {len(distance_results[0])}\n')

    print(f'{k} Recommendations:\n')

    recommendation_list = []

    recommendation_dict = {}

    # Loop until j = k

    j = 0

    # Initiate iterator for distance_results_sorted Array:
    i = 0

    # Get first result outside of loop
    # Grab the first distance from distance_results_sorted:
    entry = distance_results_sorted[i]


    # Dictionary Output:
    recommendation_index = list(distance_results[0]).index(entry)
    recommendation_dict['title'] = clustered_df.iloc[recommendation_index]['primaryTitle']
    recommendation_dict['url'] = clustered_df.iloc[recommendation_index]['url']
    recommendation_dict['releaseYear'] = clustered_df.iloc[recommendation_index]['startYear']
    recommendation_dict['averageRating'] = clustered_df.iloc[recommendation_index]['averageRating']
    recommendation_dict['genres'] = clustered_df.iloc[recommendation_index]['genres'].replace(",", ", ")

    recommendation_list.append(recommendation_dict)

    i = i + 1
    j = j + 1

    #for entry in k_min_non_zero:
    while j < k:
        
        recommendation_dict = {}
        
        if i == len(distance_results_sorted):
            break

        entry = distance_results_sorted[i]

        # Dictionary Output:
        recommendation_index = list(distance_results[0]).index(entry)
        title = clustered_df.iloc[recommendation_index]['primaryTitle']

        # If title is equal to the previous title, increment i and restart loop:

        if title == recommendation_list[j-1]['title']:
            i = i + 1
            continue

        recommendation_dict['title'] = clustered_df.iloc[recommendation_index]['primaryTitle']
        recommendation_dict['url'] = clustered_df.iloc[recommendation_index]['url']
        recommendation_dict['releaseYear'] = clustered_df.iloc[recommendation_index]['startYear']
        recommendation_dict['averageRating'] = clustered_df.iloc[recommendation_index]['averageRating']
        recommendation_dict['genres'] = clustered_df.iloc[recommendation_index]['genres'].replace(",", ", ")

        recommendation_list.append(recommendation_dict)

        j = j + 1


    # Sort recommendatioin_list by 'averageRating'
    recommendation_list = sorted(recommendation_list, key=lambda d: d['averageRating'], reverse=True)

    print(recommendation_list)

    return recommendation_list


# main for Testing

#input_movie_text = input("Movie Title: ")

#input_movie_text = "Vertigo (1958)"
#input_movie_text = "Sleepless in Seattle"
#input_movie_text = "The Killing"
#input_movie_text = "From Russia with Love"
#input_movie_text = "Toy Story"
#input_movie_text = "Goldfinger"

#print("Generating Recommendations...")

#print(get_movies(input_movie_text))

#print(get_titles()[:5])

# END
