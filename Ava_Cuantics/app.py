from flask import Flask
from models import db
from routes.auth_routes import auth_bp
from routes.course_routes import course_bp
from routes.api_routes import api_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ava_cuantics.db'
app.config['SECRET_KEY'] = 'clave-super-secreta'

db.init_app(app)

# Registrar blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(course_bp)
app.register_blueprint(api_bp)
