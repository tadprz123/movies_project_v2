import pytest
from unittest.mock import patch
import tmdb_client

# Parametryzowany test dla funkcji get_movies_list
@pytest.mark.parametrize("list_type, expected_url", [
    ("popular", "https://api.themoviedb.org/3/movie/popular"),
    ("top_rated", "https://api.themoviedb.org/3/movie/top_rated"),
    ("upcoming", "https://api.themoviedb.org/3/movie/upcoming"),
    ("now_playing", "https://api.themoviedb.org/3/movie/now_playing")
])
@patch('tmdb_client.requests.get')
def test_get_movies_list(mock_get, list_type, expected_url):
    expected_response = {"results": [{"id": 1, "title": "Test Movie"}]}
    
    mock_get.return_value.json.return_value = expected_response

    movies = tmdb_client.get_movies_list(list_type=list_type)
    
    assert movies == expected_response
    mock_get.assert_called_once_with(
        expected_url,
        headers=tmdb_client.get_headers()
    )

# Test dla funkcji get_single_movie
@patch('tmdb_client.requests.get')
def test_get_single_movie(mock_get):
    movie_id = 123
    expected_response = {"id": movie_id, "title": "Test Movie"}
    
    mock_get.return_value.json.return_value = expected_response

    movie = tmdb_client.get_single_movie(movie_id)
    
    assert movie == expected_response
    mock_get.assert_called_once_with(
        f"https://api.themoviedb.org/3/movie/{movie_id}",
        headers=tmdb_client.get_headers()
    )

# Test dla funkcji get_movie_images
@patch('tmdb_client.requests.get')
def test_get_movie_images(mock_get):
    movie_id = 123
    expected_response = {"id": movie_id, "backdrops": [], "posters": []}
    
    mock_get.return_value.json.return_value = expected_response

    images = tmdb_client.get_movie_images(movie_id)
    
    assert images == expected_response
    mock_get.assert_called_once_with(
        f"https://api.themoviedb.org/3/movie/{movie_id}/images",
        headers=tmdb_client.get_headers()
    )

# Test dla funkcji get_single_movie_cast
@patch('tmdb_client.requests.get')
def test_get_single_movie_cast(mock_get):
    movie_id = 123
    expected_response = [
        {"id": 1, "name": "Actor 1"},
        {"id": 2, "name": "Actor 2"}
    ]
    
    mock_get.return_value.json.return_value = {
        "cast": expected_response
    }

    cast = tmdb_client.get_single_movie_cast(movie_id)
    
    assert cast == expected_response
    mock_get.assert_called_once_with(
        f"https://api.themoviedb.org/3/movie/{movie_id}/credits",
        headers=tmdb_client.get_headers()
    )
