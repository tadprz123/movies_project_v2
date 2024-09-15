import pytest
from unittest.mock import patch
import tmdb_client

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
