
CREATE TABLE "title_basics" (
    CONSTRAINT "tconst" VARCHAR(10) NOT NULL PRIMARY KEY,
    "titleType" VARCHAR(5) NOT NULL,
    "primaryTitle" VARCHAR(400) NOT NULL,
    "originalTitle" VARCHAR(400) NOT NULL,
    "isAdult" INT(1) NOT NULL,
    "startYear" INT(4) NOT NULL,
    "runtimeMinutes" INT(10) NOT NULL,
    "genres" VARCHAR(50) NOT NULL
);

-- PICK UP HERE...

CREATE TABLE "US_title_ids_unique" (
    "imdb_id" VARCHAR(20)   NOT NULL,
    "genres" VARCHAR(200)   NOT NULL,
    "Title" VARCHAR(200)   NOT NULL,
    "rating" INT   NOT NULL,
    CONSTRAINT "pk_watched_list" PRIMARY KEY (
        "imdb_id"
     )
);

CREATE TABLE "title_ratings" (
    "movie_id" INT   NOT NULL,
    "avg_rating" INT   NOT NULL,
    CONSTRAINT "pk_ratings" PRIMARY KEY (
        "movie_id"
     )
);


ALTER TABLE "kaggle_metadata" ADD CONSTRAINT "fk_kaggle_metadata_id" FOREIGN KEY("id")
REFERENCES "ratings" ("movie_id");

ALTER TABLE "kaggle_metadata" ADD CONSTRAINT "fk_kaggle_metadata_imdb_id" FOREIGN KEY("imdb_id")
REFERENCES "watched_list" ("imdb_id");

