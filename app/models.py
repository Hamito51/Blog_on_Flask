from app import db
from datetime import datetime
import re


# Function for making slugs from titles, using subs for forbidden symbols
def slugify(s):
	pattern = r'[^\w+]'
	return re.sub(pattern, '-', s)

# ManyToMany
post_tags = db.Table('post_tags',
					 db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
					 db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
	)

class Post(db.Model):
	"""Structure for posts, using in out website"""
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	slug = db.Column(db.String(100), unique=True)
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		self.generate_slug()

	tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

	def generate_slug(self):
		if self.title:
			self.slug = slugify(self.title)

	def __repr__(self):
		return f'{self.title}'


class Tag(db.Model):
	"""Structure for tags, using in out website"""
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	slug = db.Column(db.String(100), unique=True)

	def __init__(self, *args, **kwargs):
		super(Tag, self).__init__(*args, **kwargs)
		self.generate_slug()

	def generate_slug(self):
		if self.name:
			self.slug = slugify(self.name)

	def __repr__(self):
		return f'{self.name}'
		


