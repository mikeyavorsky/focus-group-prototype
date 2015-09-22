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
            ],
            'comments': [
                {
                  'id': '1',
                  'timestamp': '2012-12-31 15:54:42.915204',
                  'author': 'Roger',
                  'body': 'I didn\'t really like Portland.'
                },
                {
                  'id': '2',
                  'timestamp': '2012-12-30 15:54:42.915204',
                  'author': 'Christine',
                  'body': 'The food!'
                }
            ]
        },
        {
            'id': '2',
            'timestamp': '2012-12-30 15:54:42.915204',
            'author': 'Susan',
            'body': 'I loved the Avengers movie!!',
            'questions': [
                {
                  'type': 'integer',
                  'body': 'How much did you love the Avengers movie? (1-5)'
                },
                {
                  'type': 'string',
                  'body': 'What was your favorite part?'
                }
            ],
            'comments': [
                {
                  'id': '1',
                  'timestamp': '2012-12-31 15:54:42.915204',
                  'author': 'Phyllis',
                  'body': 'I didn\'t really like the Avengers movie.'
                },
                {
                  'id': '2',
                  'timestamp': '2012-12-30 15:54:42.915204',
                  'author': 'Velociraptor',
                  'body': 'The enemies looked like dinosaurs.'
                }
            ]
        },
    ]
    return render_template('index.html',
                           title='Home',
                           posts=posts)

@app.route('/post/')
@app.route('/post/<id>')
def post():
    post = {
            'id': '2',
            'timestamp': '2012-12-30 15:54:42.915204',
            'author': 'Susan',
            'body': 'I loved the Avengers movie!!',
            'questions': [
                {
                  'type': 'integer',
                  'body': 'How much did you love the Avengers movie? (1-5)'
                },
                {
                  'type': 'string',
                  'body': 'What was your favorite part?'
                }
            ],
            'comments': [
                {
                  'id': '1',
                  'timestamp': '2012-12-31 15:54:42.915204',
                  'author': 'Phyllis',
                  'body': 'I didn\'t really like the Avengers movie.'
                },
                {
                  'id': '2',
                  'timestamp': '2012-12-30 15:54:42.915204',
                  'author': 'Velociraptor',
                  'body': 'The enemies looked like dinosaurs.'
                }
            ]
    }
    return render_template('post.html',
                           title=post['title'],
                           post=post)


@app.route('/admin')
def admin():
    return render_template('admin.html',
                           title='Admin')

@app.route('/results/<post_id>')
def results(post_id):
    post = {
            'id': '2',
            'timestamp': '2012-12-30 15:54:42.915204',
            'author': 'Susan',
            'body': 'I loved the Avengers movie!!',
            'questions': [
                {
                  'type': 'integer',
                  'body': 'How much did you love the Avengers movie? (1-5)'
                },
                {
                  'type': 'string',
                  'body': 'What was your favorite part?'
                }
            ],
            'comments': [
                {
                  'id': '1',
                  'timestamp': '2012-12-31 15:54:42.915204',
                  'author': 'Phyllis',
                  'body': 'I didn\'t really like the Avengers movie.'
                },
                {
                  'id': '2',
                  'timestamp': '2012-12-30 15:54:42.915204',
                  'author': 'Velociraptor',
                  'body': 'The enemies looked like dinosaurs.'
                }
            ]
    }
    answers = [
      {
        'id': '1',
        'question_id': '1',
        'timestamp': '2012-12-30 15:54:42.915204',
        'author': 'Susan',
        'type': 'string',
        'body': 'I answer that I loved the Avengers movie!!'
      }
    ]
    return render_template('results.html',
                           post=post,
                           answers=answers,
                           title=post['title']+' Results')

@app.route('/new-post')
def new_post():
    return render_template('new-post.html',
                           title='New Post')
