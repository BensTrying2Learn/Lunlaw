from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, SelectField, DateField, TimeField, FloatField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import DateField

class RegistrationForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	name = StringField('Full Name', validators=[DataRequired()])
	subscribe = SubmitField('Subscribe')
	description = TextField('Description')
	issue = StringField('Issue')
	submit = SubmitField('Submit')
	phone = StringField('Phone Number', validators=[DataRequired()])