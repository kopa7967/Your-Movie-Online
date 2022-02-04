import requests
import json
from bs4 import BeautifulSoup
from forms import MovieForm

class Movies():
	
	def __init__(self):
		self.DATA = {"results":""}

	def set_results(self, results):
		self.DATA["results"] = results	

	def request_movies(self):
		pass

	def load_movies(self):
		pass

	def show_movies(self):
		pass		

class SearchMovie(Movies):
	def __init__(self, url):

		Movies.__init__(self)
		self.form = MovieForm()
		self.__url = url

	def get_data(self):
		return self.DATA
		
	def request_movies(self, movie_title):
		movies = requests.get(f"{self.__url}?query_term={movie_title}")
		movies = json.loads(movies.text)
		return movies["data"]

	def load_movies(self, movie_title):
		movie_results = self.request_movies(movie_title)	
		self.set_results(movie_results)
		return self.get_data()
	

class UpcomingMovies(Movies):
	def __init__(self):
		Movies.__init__(self)
			

	def request_movies(self):
		request = requests.get("https://www.imdb.com/list/ls016522954/?ref_=ttls_ref_typ&sort=list_order,asc&st_dt=&mode=detail&page=1&title_type=movie")
		return request.text	

	def find_movies(self):
		html_doc = self.request_movies()
		soup = BeautifulSoup(html_doc, "html.parser")
		upcoming_movies = soup.find(attrs={"class": "lister-list"})
		return upcoming_movies.contents	

	def load_movies(self):
		upcoming_movies = self.find_movies()
		self.set_results(upcoming_movies)

	def get_data(self):
		self.load_movies()
		return self.DATA

