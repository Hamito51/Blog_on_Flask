from app import app
from flask import render_template, request, redirect, url_for
from posts.blueprint import index
from models import Post


@app.route('/')
def index():
	return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')




