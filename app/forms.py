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

class AnswerForm(Form):
    author = StringField('author', validators=[DataRequired()])
    a0 = TextAreaField('a0', validators=[DataRequired()])
    a1 = TextAreaField('a1')
    a2 = TextAreaField('a2')
    a3 = TextAreaField('a3')
    a4 = TextAreaField('a4')
    a5 = TextAreaField('a5')
    a6 = TextAreaField('a6')
    a7 = TextAreaField('a7')
    a8 = TextAreaField('a8')
    a9 = TextAreaField('a9')
    a10 = TextAreaField('a10')
    a11 = TextAreaField('a11')
    a12 = TextAreaField('a12')
    a13 = TextAreaField('a13')
    a14 = TextAreaField('a14')
    a15 = TextAreaField('a15')
    a16 = TextAreaField('a16')
    a17 = TextAreaField('a17')
    a18 = TextAreaField('a18')
    a19 = TextAreaField('a19')

class DeleteForm(Form):
    post_id_to_delete = StringField('post_id_to_delete', validators=[DataRequired()])
