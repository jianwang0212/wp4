from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Required
from flaskblog.models import User, Category
from wtforms.widgets import ListWidget, CheckboxInput
from flaskblog import app, db, bcrypt


class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


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
            raise ValidationError(
                'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class QuestionsForm(FlaskForm):
    answer_1 = MultiCheckboxField('Which label best applies?', choices=[])
    submit = SubmitField('submit answers')


class LabelDeleteForm(FlaskForm):
    answer_1 = MultiCheckboxField(
        'Which label do you want to delete?', choices=[])
    submit = SubmitField('submit answers')


class CategoryForm(FlaskForm):
    category = StringField(
        'What category do you want to add into the ML annotation?')
    submit = SubmitField('submit answers')


class CategoryDeleteForm(FlaskForm):
    category_delete = MultiCheckboxField(
        'Which category do you want to delete? ', choices=[])
    submit = SubmitField('submit answers')


class KeywordForm(FlaskForm):
    keyword = StringField('What keyword do you want to add?')
    submit = SubmitField('submit keyword')


class KeywordDeleteForm(FlaskForm):
    keyword_delete = MultiCheckboxField(
        'Which keyword do you want to delete? ', choices=[])
    submit = SubmitField('submit answers')
