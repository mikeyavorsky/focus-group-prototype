from flask import render_template, flash, redirect
from app import app
from .models import Post, Comment, Question, Answer, Response


@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html',
                           title='Home',
                           posts=posts)

@app.route('/post/')
@app.route('/post/<post_id>')
def post(post_id=0):
    if post_id == 0:
        post = Post.query.order_by(Post.timestamp.desc())
    else:
        post = Post.query.filter_by(id=post_id)
    #post = Post.query.order_by(Post.timestamp.desc()).first()
    return render_template('post.html',
                           title=post[0].title,
                           post=post[0])


@app.route('/admin')
def admin():
    return render_template('admin.html',
                           title='Admin')

@app.route('/results/<post_id>')
def results(post_id=0):
    if post_id == 0:
        post = Post.query.order_by(Post.timestamp.desc())
    else:
        post = Post.query.filter_by(id=post_id)
    questions = Question.query.filter_by(post_id=post[0].id)
    relevant_answers = []
    for question in questions:
        answers = Answer.query.filter_by(question_id=question.id)
        for answer in answers:
            relevant_answers.append(answer)
    return render_template('results.html',
                           post=post[0],
                           questions=questions,
                           answers=relevant_answers,
                           title=post[0].title+' Results')

@app.route('/new-post')
def new_post():
    return render_template('new-post.html',
                           title='New Post')
