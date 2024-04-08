from fastapi import FastAPI
import csv

app = FastAPI()


class Movie:
    def __init__(self, movie_id, title, genres):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres


@app.get("/test")
def read_root():
    return {"Hello": "World"}


@app.get("/movies")
def get_movies():
    movies = []
    with open('movies.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if isinstance(row, dict):
                movie_id = row.get('movieId')
                title = row.get('title')
                genres = row.get('genres')
                movie = Movie(movie_id, title, genres)
                movies.append(movie.__dict__)
    return movies
