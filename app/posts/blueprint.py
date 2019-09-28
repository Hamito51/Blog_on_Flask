from flask import Blueprint, render_template
from app import app


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    return render_template('posts/index.html', posts=posts)
