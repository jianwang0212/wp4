from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, QuestionsForm, CategoryForm, KeywordForm, CategoryDeleteForm
from flaskblog.models import User, Post, Test, Category, Keyword
from sqlalchemy.orm import load_only

# read from csv file as posts
import pandas as pd
df = pd.read_excel('oxfordshire_lep_with_text.xlsx',
                   sheet_name='Construction 2019')
df = df.dropna(subset=['JobText'])
df = df
df = df[['JobID', 'JobText']]
df_list = df.values.tolist()
posts = []
for i in df_list:
    # print i[0]
    element = {
        'JobID': i[0],
        'JobText': i[1]
    }
    posts.append(element)


# construct the category
old_categories = [('Industry 4.0', 'Industry 4.0'), ('Oxfordshire Plumbing',
                                                     'Oxfordshire Plumbing'), ('Engineering Construction', 'Engineering Construction')]
old_categories_list = ['Industry 4.0',
                       'Oxfordshire Plumbing', 'Engineering Construction']


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    labels = Test.query.all()
    keywords = Keyword.query.all()

    return render_template('home.html', posts=posts, labels=labels, keywords=keywords)


@app.route("/category", methods=['GET', 'POST'])
def category():
    form = CategoryForm()
    categories_list = old_categories_list + \
        [category.category
         for category in Category.query.all()]

    if form.validate_on_submit():
        answer = Category(category=form.category.data)
        db.session.add(answer)
        db.session.commit()
        flash('New category has been saved', 'success')
        return redirect(url_for('home'))

    return render_template('category.html', posts=posts, form=form, labels=categories_list)


@app.route("/category/delete", methods=['GET', 'POST'])
def category_delete():
    form = CategoryDeleteForm()
    categories_list = old_categories_list + \
        [category.category
         for category in Category.query.all()]
    form.category_delete.choices = old_categories + \
        [(category.category, category.category)
         for category in Category.query.all()]
    if form.validate_on_submit():
        list_to_delete = form.category_delete.data
        for string in list_to_delete:
            delete_this = Category.query.filter_by(
                category=string).first()
            db.session.delete(delete_this)
            db.session.commit()

        flash('Deleted', 'success')
        return redirect(url_for('home'))

    return render_template('category_delete.html', posts=posts, form=form, labels=categories_list)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode("utf-8")
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login uncessful', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/test/<test_id>", methods=['GET', 'POST'])
def test(test_id):
    post = next(item for item in posts if item["JobID"] == int(
        test_id))  # select the post that match the ID
    form = QuestionsForm()
    form.answer_1.choices = old_categories + \
        [(category.category, category.category)
         for category in Category.query.all()]
    if form.validate_on_submit():
        answers = form.answer_1.data
        for answer in answers:
            # change a list to a string
            answer = Test(jobID=int(test_id), answer_1=answer)
            db.session.add(answer)
            db.session.commit()
        flash('Your answer has been saved', 'success')
        return redirect(url_for('home'))

    return render_template('test.html', post=post, title='test', form=form)


@app.route("/test/<test_id>/clear_label", methods=['GET', 'POST'])
def test_delete(test_id):

    labels = Test.query.filter_by(
        jobID=int(test_id)).all()
    print(labels)
    for label in labels:
        db.session.delete(label)
        db.session.commit()
    flash('Deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/keyword<keyword_id>", methods=['GET', 'POST'])
def keyword(keyword_id):
    post = next(item for item in posts if item["JobID"] == int(keyword_id))
    form = KeywordForm()
    if form.validate_on_submit():
        answer = Keyword(jobID=int(keyword_id), keyword=form.keyword.data)
        db.session.add(answer)
        db.session.commit()
        flash('Keyword has been saved', 'success')
        return redirect(url_for('home'))

    return render_template('keyword.html', post=post, form=form)
