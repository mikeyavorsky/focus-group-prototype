from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class PostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    timestamp = datetime.datetime.utcnow
    post = StringField('post', validators=[DataRequired()])
