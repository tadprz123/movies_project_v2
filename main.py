from flask import Flask, render_template, request
import tmdb_client
import random

app = Flask(__name__)

MOVIE_LISTS = ['now_playing', 'popular', 'top_rated', 'upcoming']

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    movies = tmdb_client.get_movies_list(selected_list)
    if "results" in movies:
        shuffled_movies = random.sample(movies["results"], len(movies["results"]))
        selected_movies = shuffled_movies[:8]
    else:
        selected_movies = []

    return render_template("homepage.html", movies=selected_movies, current_list=selected_list, movie_lists=MOVIE_LISTS)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops']) if movie_images['backdrops'] else None

    return render_template("movie_details.html", movie=details, cast=cast, backdrop=selected_backdrop)

if __name__ == '__main__':
    app.run(debug=True)
