from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' # can change this to your preferred database path

    db.init_app(app)
    from .views import views
    app.register_blueprint(views)

    return app

#import app.views
