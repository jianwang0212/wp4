from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm,QuestionsForm,CategoryForm
from flaskblog.models import User, Post, Test, Category


import pandas as pd
df = pd.read_excel('oxfordshire_lep_with_text.xlsx', sheet_name = 'Construction 2019')
df = df.dropna(subset=['JobText'])
df = df
df = df[['JobID','JobText']]
df_list = df.values.tolist()
posts =[]
for i in df_list:
    # print i[0]
    element = {
        'JobID': i[0],
        'JobText': i[1]
    }
    posts.append(element)



@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts = posts)

@app.route("/category", methods = ['GET','POST'])
def category():
	form = CategoryForm()
	if form.validate_on_submit():
		answer = Category(category = form.category.data)
		db.session.add(answer)
		db.session.commit()
		flash('Your answer has been saved', 'success')
		return redirect(url_for('home'))

	return render_template('category.html', posts = posts,form = form)

@app.route("/register", methods = ['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
		user = User(username = form.username.data, email = form.email.data, password = hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET','POST'])
@app.route("/login")
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data =='password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login uncessful', 'danger')
	return render_template('login.html', title = 'Login', form = form)

@app.route("/test/<test_id>", methods = ['GET','POST'])
def test(test_id):
	print(test_id)
	post = next(item for item in posts if item["JobID"] == int(test_id))

	form = QuestionsForm()
	if form.validate_on_submit():
		answer = Test(jobID = int(test_id), answer_1 = form.answer_1.data)
		db.session.add(answer)
		db.session.commit()
		flash('Your answer has been saved', 'success')
		return redirect(url_for('home'))

	return render_template('test.html', post = post,title = 'test', form = form)


