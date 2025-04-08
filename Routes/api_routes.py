from flask import Blueprint, jsonify
from models import Course

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/courses')
def get_courses():
    courses = Course.query.all()
    data = [{
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'price': course.price,
        'filename': course.filename
    } for course in courses]
    return jsonify(data)
