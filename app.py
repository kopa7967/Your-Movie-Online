from flask import Flask, render_template
import requests
import movies


app = Flask(__name__)

SECRET_KEY = ""
app.config["SECRET_KEY"] = SECRET_KEY

@app.route("/", methods=['GET', 'POST'])
def index():
	try:
		search_movie = movies.SearchMovie("https://yts.mx/api/v2/list_movies.json")

		if search_movie.form.validate_on_submit():
			search_movie.load_movies(search_movie.form.movie.data)

		return render_template("index.html", data=search_movie)
	except:
		return "ERROR"
		
@app.route("/upcoming_vod/")
def upcoming_vod():
	upcoming_movies = movies.UpcomingMovies()

	return render_template("upcoming_vod.html", data=upcoming_movies)

if __name__ == "__main__":
	app.run()
