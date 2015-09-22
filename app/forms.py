from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, RadioField, IntegerField
from wtforms.validators import DataRequired
from datetime import datetime

class CommentForm(Form):
    author = StringField('author', validators=[DataRequired()])
    body = StringField('body', validators=[DataRequired()])

class PostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    body = StringField('body', validators=[DataRequired()])
    num_questions = IntegerField('num_questions')

class AddQuestionForm(Form):
    type = RadioField(u'Type', choices=[
        ('1', u'You want the respondent to write out an answer.'),
        ('2', u'You want the respondent to rank something from 1 to 5.')],
        default='1', validators=[DataRequired()])
    body = StringField('body', validators=[DataRequired()])
