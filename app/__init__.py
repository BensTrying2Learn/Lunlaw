from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ed877060e79b251f805cc14ffdddbff1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://brand335:335Benben@aa1aj3aw9s5oyiq.ci8qx4d4reut.us-west-2.rds.amazonaws.com/lunlaw_db'

db = SQLAlchemy()
bcrypt = Bcrypt(app)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'bensdrive89@gmail.com'
app.config['MAIL_PASSWORD'] = '335Benben'
SQLALCHEMY_TRACK_MODIFICATIONS = True

mail = Mail(app)

from app import routes