-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "g_mvs_title_basics" (
    "tconst" varchar(10)   NOT NULL,
    "titletype" varchar(5)   NOT NULL,
    "primarytitle" varchar(250)   NOT NULL,
    "originaltitle" varchar(250)   NOT NULL,
    "isadult" int   NOT NULL,
    "startyear" int   NOT NULL,
    "runtimeminutes" int   NOT NULL,
    "genres" varchar(50)   NOT NULL,
	CONSTRAINT "pk_g_mvs_title_basics" PRIMARY KEY (
        "tconst"
     )
);

CREATE TABLE "g_mvs_us_title_ids" (
    "tconst" varchar(10)   NOT NULL,
	CONSTRAINT "pk_g_mvs_us_title_ids" PRIMARY KEY (
        "tconst"
     )
);

CREATE TABLE "g_mvs_title_ratings" (
    "tconst" varchar(10)   NOT NULL,
    "averagerating" float   NOT NULL,
    "numvotes" int   NOT NULL,
	CONSTRAINT "pk_g_mvs_title_ratings" PRIMARY KEY (
        "tconst"
     )
);

--ALTER TABLE "g_mvs_us_title_ids" ADD CONSTRAINT "fk_g_mvs_us_title_ids_tconst" FOREIGN KEY("tconst")
--REFERENCES "g_mvs_title_basics" ("tconst");

--ALTER TABLE "g_mvs_title_ratings" ADD CONSTRAINT "fk_g_mvs_title_ratings_tconst" FOREIGN KEY("tconst")
--REFERENCES "g_mvs_title_basics" ("tconst");

