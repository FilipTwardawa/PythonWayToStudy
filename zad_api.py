from fastapi import FastAPI
import csv

app = FastAPI()


class Movie:
    def __init__(self, movie_id, title, genres):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id


class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp


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


@app.get("/links")
def get_links():
    links = []
    with open('links.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if isinstance(row, dict):
                link = Link(row.get('movieId'), row.get('imdbId'), row.get('tmdbId'))
                links.append(link.__dict__)
    return links


@app.get("/ratings")
def get_ratings():
    ratings = []
    with open('ratings.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if isinstance(row, dict):
                rating = Rating(row.get('userId'), row.get('movieId'), row.get('rating'), row.get('timestamp'))
                ratings.append(rating.__dict__)
    return ratings


@app.get("/tags")
def get_tags():
    tags = []
    with open('tags.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if isinstance(row, dict):
                tag = Tag(row.get('userId'), row.get('movieId'), row.get('tag'), row.get('timestamp'))
                tags.append(tag.__dict__)
    return tags
