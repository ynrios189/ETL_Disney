DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS directors;
DROP TABLE IF EXISTS movies;
CREATE TABLE "characters" (
    "Movie_Title" VARCHAR PRIMARY KEY ,
    "Release_Date" VARCHAR,
    "Hero" VARCHAR,
    "Villain" VARCHAR,
    "Song" VARCHAR
);
CREATE TABLE "directors" (
    "Movie_Title" VARCHAR PRIMARY KEY ,
    "Director" VARCHAR
);
CREATE TABLE "movies" (
    "Movie_Title" VARCHAR,
    "Release_Date" VARCHAR,
    "Genre" VARCHAR,
    "MPAA_Rating" VARCHAR,
    "Total_Gross" VARCHAR,
    "Inflation_Adjusted_Gross" VARCHAR
);