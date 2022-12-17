from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
app.config['SECRET_KEY'] = 'a02c6cf1c0b6d849ffaa0b3f'
db = SQLAlchemy(app)



from market import routes
