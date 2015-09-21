from flask import render_template, flash, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'id': '1',
            'timestamp': '2012-12-31 15:54:42.915204',
            'author': 'John',
            'body': 'Beautiful day in Portland!',
            'questions': [
                {
                  'type': 'integer',
                  'body': 'how much do you love Portland (1-5)?'
                },
                {
                  'type': 'string',
                  'body': 'What do you love most about Portland?'
                }
            ]
        },
        {
            'id': '2',
            'timestamp': '2012-12-30 15:54:42.915204',
            'author': 'Susan',
            'body': 'The Avengers movie was so cool!',
            'questions': [
                {
                  'type': 'integer',
                  'body': 'how much do you love Portland (1-5)?'
                },
                {
                  'type': 'string',
                  'body': 'What do you love most about Portland?'
                }
            ] 
        }
    ]
    comments = [
        {
            'id': '1',
            'post_id': '2',
            'timestamp': '2012-12-31 15:54:42.915204',
            'author': 'Roger',
            'body': 'I didn't really like the Avengers movie, nor seeing it in Portland.'
        },
        {
            'id': '2',
            'post_id': '1',
            'timestamp': '2012-12-30 15:54:42.915204',
            'author': 'Christine',
            'body': 'I loved the food in Portland! Shwarma! Just like the Avengers'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           posts=posts
                           comments=comments)

@app.route('/post/')
@app.route('/post/<id>')
def post():
    post = [
        {
            'id': '2',
            'timestamp': '2012-12-30 15:54:42.915204',
            'author': 'Susan',
            'body': 'The Avengers movie was so cool!',
            'questions': [
                {
                  'type': 'integer',
                  'body': 'how much do you love Portland (1-5)?'
                },
                {
                  'type': 'string',
                  'body': 'What do you love most about Portland?'
                }
            ]
        }
    ]
    comments = [
        {
            'id': '1',
            'post_id': '2',
            'author': 'Roger',
            'body': 'I didn't really like the Avengers movie, nor seeing it in Portland.'
        }
    ]
    return render_template('post.html',
                           title=post['title'],
                           post=post,
                           comments=comments)
