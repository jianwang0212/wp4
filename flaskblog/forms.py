from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField,RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class QuestionsForm(FlaskForm):
    answer_1 = RadioField('Which label best applies?',choices=[('Industry 4.0', 'Industry 4.0'), ('Oxfordshire Plumbing', 'Oxfordshire Plumbing'),('Engineering Construction', 'Engineering Construction')])
    # answer_2 = RadioField('Does this passage contain information about ZHC2?',choices=[('yes', 'Yes'), ('no', 'No')])

    submit = SubmitField('submit answers')

class CategoryForm(FlaskForm):
    category = StringField('What category do you want to add into the ML annotation?')
    # answer_2 = RadioField('Does this passage contain information about ZHC2?',choices=[('yes', 'Yes'), ('no', 'No')])

    submit = SubmitField('submit answers')

class KeywordForm(FlaskForm):
    keyword = StringField('What keyword do you want to add?')
    # answer_2 = RadioField('Does this passage contain information about ZHC2?',choices=[('yes', 'Yes'), ('no', 'No')])

    submit = SubmitField('submit keyword')


