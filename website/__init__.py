from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '3e89a5fec09ceabb770571cac2a32d10'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.root_path}/site.db"


    db.init_app(app)

    from .views import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note 
    create_database(app)

    return app


def create_database(app): 
    if not path.exists('website/' + DB_NAME): 
        # Create the database (if it doesn't exist)
        with app.app_context():
            db.create_all()        
        print('Database Created!')
    