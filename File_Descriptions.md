
Root Directory:

| File Name                                                                    | Brief Description of Contents
|------------------------------------------------------------------------------|------------------------------
| `app.py`                                                                     | Python Flask App which runs model.py (Connects to AWS RDS)
| `app_local.py`                                                               | Python Flask App which runs `model_local.py` (Retrieves Data from Delimited Flat Files in `Data` Directory)
| `AWS_Test.ipynb`                                                             | Jupyter Notebook to Test Connection to AWS RDS
| `File_Descriptions.md`                                                       | Descriptions of File Contents in Markdown Table Format
| `g-mvs-CreateTables.sql`                                                     | Original pgAdmin SQL Script to Create Tables with Original Source Data (Unused)
| `g-mvs_Hierarchical_Clustering_ML_Model_v2_with_Recommendations.ipynb`       | Jupyter Notebook to Test Hierarchical Clustering Algorithm, and evaluate model results
| `g-mvs_K-Means_ML_Model_v4_with_Recommendations.ipynb`                       | Jupyter Notebook to Test K-Means Clustering Algorithm
| `g-mvs_K-Means_ML_Model_v4_with_Recommendations_TRAINING.ipynb`              | Jupyter Notebook to Test K-Means Clustering Algorithm, and evaluate model results
| `gmvsDATAUpload.py`                                                          | Python Script to Upload Local Delimited Flat Files to AWS RDS PostgreSQL Database
| `g_mvs_create_table-V 1.3.sql`                                               | Final pgAdmin SQL Script to Create Tables with Final Source Data (Used)
| `model.py`                                                                   | Final Project Python Source Code which retrieves Final Source Data from AWS RDS and runs K-Means Clustering Algorithm
| `model_local.py`                                                             | Final Project Python Source Code which retrieves Final Source Data from Local Delimited Flat Files and runs K-Means Clustering Algorithm
| `model_local_CMD.py`                                                         | Final Project Python Source Code which retrieves Final Source Data from Local Delimited Flat Files and runs K-Means Clustering Algorithm. Formatted output sent directly to Terminal.
| `README.md`                                                                  | README Project Description for GitHub Repository
| `Speaking Notes.docx`                                                        | Notes for Speakers to refer to during Presentation


Autocomplete(attempted) Directory:

| File Name                                                                    | Brief Description of Contents
|------------------------------------------------------------------------------|------------------------------
| `app.py`                                                                     | 
| `app_2.py`                                                                   | 
| `app_localAC.py`                                                             | 
| `index_1.html`                                                               | 
| `index_2.html`                                                               | 
| `index_3.html`                                                               | 
| `index_4.html`                                                               | 
| `index_5.html`                                                               | 
| `index_6.html`                                                               | 
| `index_7.html`                                                               | 
| `index_local_2.html`                                                         | 
| `txt_validation\app_txt_validation.py`                                       | 
| `txt_validation\data\movies.txt`                                             | 
| `txt_validation\templates\index.html`                                        | 


Data Directory:

| File Name                                                                    | Brief Description of Contents
|------------------------------------------------------------------------------|------------------------------
| `K-Means_Model_Output.tsv`                                                   | Archived Output of K-Means Clustering Algorithm for Database Testing
| `movies_df_sample.csv`                                                       | Archived 1,001 Row Output of `movies_df` Pandas DataFrame for Database Testing
| `title_basics_non-adult_movies.tsv`                                          | Trimmed Dataset from IMDb, rows including Null Values '\N' retained.
| `title_basics_non-adult_movies_no_nulls.tsv`                                 | Trimmed Dataset from IMDb, Null Values excluded.
| `title_ratings.csv`                                                          | Original Ratings Dataset from IMDb, converted from TSV to CSV
| `US_title_ids_unique.csv`                                                    | Extracted unique list of US Title IDs from Original IMDb `title.akas.tsv` Dataset


Images Directory:

| File Name                                                                    | Brief Description of Contents
|------------------------------------------------------------------------------|------------------------------
| `g_mvs ERD.png`                                                              | Image of Final AWS RDS Entity-Relationship Diagram
| `image.png`                                                                  | Intermediate version of AWS RDS ERD
| `image_updated.png`                                                          | Revised version of AWS RDS ERD
| `movies_recommendation_engine_goldfinger.png`                                | Screenshot of Model Output to HTML Dashboard
| `movies_recommendation_engine_toy_story.png`                                 | Screenshot of Model Output to HTML Dashboard
| `Technologies used.png`                                                      | Screenshot of Technologies Used Table for README.md


Metadata Directory:

| File Name                                                                    | Brief Description of Contents
|------------------------------------------------------------------------------|------------------------------
| `title_basics_non-adult_movies_genres_uniq.txt`                              | List of Genres from IMDb Source Data
| `WatchED_List_genres_uniq.txt`                                               | List of Genres from old Dataset to compare against new Dataset


Resources Directory:

| File Name                                                                    | Brief Description of Contents
|------------------------------------------------------------------------------|------------------------------
| `Data_Mapping.xlsx`                                                          | Descriptions of Data Fields in Local Flat Files to Assist in Generating RDS ERD
| `Final-Project-G-V1.0.docx`                                                  | Initial Design Document Outlining Project Features and Goals Prior to Beginning Project Work
| `g-mvs-Final-Project Details-V1.0.docx`                                      | Intermediate Design Document Following Project Goals Revision
| `ML_Flowchart_v1.pptx`                                                       | Initial Flowchart of Intended Machine Learning Model Prior to Beginning Project Work
| `UI_Flowchart_v1.pptx`                                                       | Initial Flowchart of User Interface Prior to Beginning Project Work
| `UI_Flowchart_v2.pptx`                                                       | Final Flowchart of User Interface at End of Project Work


static Directory:

| File Name                                                                    | Brief Description of Contents
|------------------------------------------------------------------------------|------------------------------
| `css\style.css`                                                              | CSS Styling for HTML Dashboard
| `images\favicon.ico`                                                         | Letter G Browser Favicon for Running HTML Dashboard


templates Directory:

| File Name                                                                    | Brief Description of Contents
|------------------------------------------------------------------------------|------------------------------
| `index.html`                                                                 | HTML Template for AWS RDS Version of app.py
| `index_local.html`                                                           | HTML Template for Local Flat Files Version of `app_local.py`


Workflows Directory:

| File Name                                                                    | Brief Description of Contents
|------------------------------------------------------------------------------|------------------------------
| `Exploratory_Data_Analysis_Steps.txt`                                        | Detailed written notes of where and when original source data was obtained, how these files were renamed, and how they were initially filtered using Command Line Tools
| `pgAdmin_Database_Tables_Creation.txt`                                       | Document detailing steps to use pgAdmin SQL Script to create Tables before Inserting Data into Database
| `title_basics_tsv_CLEANING.txt`                                              | Detailed written notes of how Command Line Tools were used to filter Original Source Data from IMDb prior to Exploratory Data Analysis using Python
