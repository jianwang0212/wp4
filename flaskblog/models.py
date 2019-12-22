from flaskblog import db
from datetime import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique=True, nullable = False)
	email = db.Column(db.String(120), unique=True, nullable = False)
	image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
	password = db.Column(db.String(60),  nullable = False)
	posts = db.relationship('Post', backref='author',lazy=True)

	def __repr__(self):
		return self.username



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return self.title

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jobID = db.Column(db.Integer)
    answer_1 = db.Column(db.Text, nullable=False)
    # answer_2 = db.Column(db.Integer, nullable=False)
    # time_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return self.answer_1

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return self.category


class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return self.category

