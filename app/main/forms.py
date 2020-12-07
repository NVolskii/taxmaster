from flask_wtf import FlaskForm
from flask_login import current_user
from app import db
from app.models import MetersReader
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    electricity = FloatField('Electricity', validators=[DataRequired()])
    cold_water = FloatField('Cold_water', validators=[DataRequired()])
    hot_water = FloatField('Hot_water', validators=[DataRequired()])
    submit = SubmitField('Send')
