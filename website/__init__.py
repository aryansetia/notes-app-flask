from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '3e89a5fec09ceabb770571cac2a32d10'

    return app