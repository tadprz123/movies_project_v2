import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNjRkYjQ5ZTQ4OWFkY2QyMzYyNzM1YTAwZTJkMWE1NiIsIm5iZiI6MTcyNDM0NDU1OS4yOTc2NCwic3ViIjoiNjZjNzY4MzBkZjBiNWE3ZDMzMTU4YmYyIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.6s35o_VVvCLtNimgkiQvEtN_upkk6JG2tJSLzJqevdI"  # Uzupełnij swoim tokenem API

def get_headers():
    return {
        "Authorization": f"Bearer {API_TOKEN}"
    }

def get_movies_list(list_type="popular"):
    url = f"https://api.themoviedb.org/3/movie/{list_type}"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(endpoint, headers=get_headers())
    response.raise_for_status()
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response = requests.get(endpoint, headers=get_headers())
    response.raise_for_status()
    return response.json()["cast"]

def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_path}"

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    response = requests.get(endpoint, headers=get_headers())
    response.raise_for_status()
    return response.json()
