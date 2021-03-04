from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db, app
import datetime

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), nullable=False)
	issue = db.Column(db.String(60), nullable=False)
	description = db.Column(db.String(1000), nullable=False)
	phone = db.Column(db.String(10), nullable=False)