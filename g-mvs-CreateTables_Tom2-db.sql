-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "kaggle_metadata" (
    "id" INT   NOT NULL,
    "genres" VARCHAR(200)   NOT NULL,
    "imdb_id" VARCHAR(20)   NOT NULL,
    "Title" VARCHAR(200)   NOT NULL,
    CONSTRAINT "pk_kaggle_metadata" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "ratings" (
    "movie_id" INT   NOT NULL,
    "avg_rating" INT   NOT NULL,
    CONSTRAINT "pk_ratings" PRIMARY KEY (
        "movie_id"
     )
);

CREATE TABLE "watched_list" (
    "imdb_id" VARCHAR(20)   NOT NULL,
    "genres" VARCHAR(200)   NOT NULL,
    "Title" VARCHAR(200)   NOT NULL,
    "rating" INT   NOT NULL,
    CONSTRAINT "pk_watched_list" PRIMARY KEY (
        "imdb_id"
     )
);

ALTER TABLE "kaggle_metadata" ADD CONSTRAINT "fk_kaggle_metadata_id" FOREIGN KEY("id")
REFERENCES "ratings" ("movie_id");

ALTER TABLE "kaggle_metadata" ADD CONSTRAINT "fk_kaggle_metadata_imdb_id" FOREIGN KEY("imdb_id")
REFERENCES "watched_list" ("imdb_id");

