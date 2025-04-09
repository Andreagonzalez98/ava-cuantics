# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def init_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    from .routes import main
    from .auth import auth_bp

    app.register_blueprint(main)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app

app = init_app()
