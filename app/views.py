from flask import render_template, flash, redirect, url_for
from app import app, db
from .models import Post, Comment, Question, Answer, Response
from .forms import PostForm, CommentForm, QuestionForm, AnswerForm, DeleteForm
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
def post(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(post_id=Post.query.order_by(Post.timestamp.desc())[0].id,
                          author=form.author.data,
                          body=form.body.data)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted!')
        return redirect(url_for('post', post_id=post_id))
    if post_id == None:
        post = Post.query.order_by(Post.timestamp.desc())
    else:
        post = Post.query.filter_by(id=post_id)
    return render_template('post.html',
                           title=post[0].title,
                           post=post[0],
                           form=form)

@app.route('/delete', methods=['GET','POST'])
@app.route('/delete/<post_id_to_delete>', methods=['GET','POST'])
def delete():
	posts = Post.query.all()
	form = DeleteForm()
	if form.validate_on_submit():
		post_to_delete = Post.query.order_by(post_id=post_id_to_delete).first()
		db.session.delete(post_to_delete)
		db.session.commit()
		flash('That post has been deleted')
		return redirect(url_for('admin'))
	return render_template('delete.html',
				title='Delete',
				posts=posts)


@app.route('/admin')
def admin():
    posts = Post.query.all()
    return render_template('admin.html',
                           title='Admin',
                           posts=posts)

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

@app.route('/new-post/', methods=['GET', 'POST'])
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
                            body=form.body.data)
        db.session.add(question)
        db.session.commit()
        flash('You\'ve added a question!')
        return redirect(url_for('admin'))
    return render_template('new-question.html',
                           title='New Question',
                           form=form)


@app.route('/answer/<post_id>', methods=['GET','POST'])
def answer(post_id):
    form = AnswerForm()
    if form.validate_on_submit():
        post = Post.query.filter_by(id=post_id)
        questions = post[0].questions
        numq = questions.count()
        response = Response(author=form.author.data)
        db.session.add(response)
        db.session.commit()
        response = Response.query.order_by(Response.timestamp.desc())
        response_id = response[0].id
        i = 0
        if(numq > 0):
            a0 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a0.data)
            db.session.add(a0)
            i += 1
        if(numq > 1):
            a1 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a1.data)
            db.session.add(a1)
            i += 1
        if(numq > 2):
            a2 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a2.data)
            db.session.add(a2)
            i += 1
        if(numq > 3):
            a3 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a3.data)
            db.session.add(a3)
            i += 1
        if(numq > 4):
            a4 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a4.data)
            db.session.add(a4)
            i += 1
        if(numq > 5):
            a5 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a5.data)
            db.session.add(a5)
            i += 1
        if(numq > 6):
            a6 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a6.data)
            db.session.add(a6)
            i += 1
        if(numq > 7):
            a7 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a7.data)
            db.session.add(a7)
            i += 1
        if(numq > 8):
            a8 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a8.data)
            db.session.add(a8)
            i += 1
        if(numq > 9):
            a9 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a9.data)
            db.session.add(a9)
            i += 1
        if(numq > 10):
            a10 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a10.data)
            db.session.add(a10)
            i += 1
        if(numq > 11):
            a11 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a11.data)
            db.session.add(a11)
            i += 1
        if(numq > 12):
            a12 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a12.data)
            db.session.add(a12)
            i += 1
        if(numq > 13):
            a13 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a13.data)
            db.session.add(a13)
            i += 1
        if(numq > 14):
            a14 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a14.data)
            db.session.add(a14)
            i += 1
        if(numq > 15):
            a15 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a15.data)
            db.session.add(a15)
            i += 1
        if(numq > 16):
            a16 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a16.data)
            db.session.add(a16)
            i += 1
        if(numq > 17):
            a17 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a17.data)
            db.session.add(a17)
            i += 1
        if(numq > 18):
            a18 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a18.data)
            db.session.add(a18)
            i += 1
        if(numq > 19):
            a19 = Answer(question_id=questions[i].id,
                        response_id=response_id,
                        type=questions[i].type,
                        body=form.a19.data)
            db.session.add(a19)
            i += 1
        db.session.commit()
        flash('Thanks for answering those questions!!')
        return redirect(url_for('post', post_id=post[0].id))
    post = Post.query.filter_by(id=post_id)
    num = post[0].questions.count()
    return render_template('answer.html',
                           title='Answer Questions',
                           post=post[0],
                           form=form,
                           questions=post[0].questions,
                           num=num)
