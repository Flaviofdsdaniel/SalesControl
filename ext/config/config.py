
from flask_sqlalchemy import SQLAlchemy


def init_app(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sale.db'

    db = SQLAlchemy(app)
