from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from common.routes import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import *
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)