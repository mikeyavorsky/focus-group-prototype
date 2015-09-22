from flask import render_template, flash, redirect, url_for
from app import app, db
from .models import Post, Comment, Question, Answer, Response
from .forms import PostForm, CommentForm, QuestionForm
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    #form = CommentForm()
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html',
                           title='Home',
                           posts=posts)

@app.route('/post/', methods=['GET','POST'])
@app.route('/post/<post_id>', methods=['GET','POST'])
def post(post_id=0):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(post_id=Post.query.order_by(Post.timestamp.desc())[0].id,
                          author=form.author.data,
                          body=form.body.data)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted!')
        return redirect(url_for('post', post_id=post_id))
    if post_id == 0:
        post = Post.query.order_by(Post.timestamp.desc())
    else:
        post = Post.query.filter_by(id=post_id)
    return render_template('post.html',
                           title=post[0].title,
                           post=post[0],
                           form=form)


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

@app.route('/new-post', methods=['GET','POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    author=form.author.data,
                    body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('admin'))
    return render_template('new-post.html',
                           title='New Post',
                           form=form)

@app.route('/new-question', methods=['GET','POST'])
def new_question():
    form = QuestionForm()
    if form.validate_on_submit():
        posts = Post.query.order_by(Post.timestamp.desc())
        post_id = posts[0].id
        question = Question(post_id=post_id,
                            type=form.qtype.data,
                            body=form.content.data)
        db.session.add(question)
        db.session.commit()
        flash('You\'ve added a question!')
        return redirect(url_for('admin'))
    return render_template('new-question.html',
                           title='New Question',
                           form=form)
