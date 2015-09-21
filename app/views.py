from flask import render_template, flash, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': 'John',
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': 'Susan',
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           posts=posts)

@app.route('/post/')
@app.route('/post/<id>')
def post():
    post = {
            'author': 'Mike',
            'title': 'Test Post',
            'body': 'This is the only post in this list of dicts'
    }
    return render_template('post.html',
                           title=post['title'],
                           post=post)
