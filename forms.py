from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
	movie = StringField("What's the movie are you looking for? ", validators=[DataRequired()])