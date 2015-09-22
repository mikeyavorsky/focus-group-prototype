from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, RadioField, IntegerField, TextAreaField
from wtforms.validators import DataRequired
from datetime import datetime

class CommentForm(Form):
    author = StringField('author', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])

class PostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])

class QuestionForm(Form):
    qtype = RadioField(u'Type', choices=[
        ('1', u'You want the respondent to write out an answer.'),
        ('2', u'You want the respondent to rank something from 1 to 5.')],
        default='1', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])
