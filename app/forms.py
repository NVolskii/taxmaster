from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class InputForm(FlaskForm):
    electricity = FloatField('Electricity')
    cold_water = FloatField('Cold_water')
    hot_water = FloatField('Hot_water')
    submit = SubmitField('Send')