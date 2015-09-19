from app import db

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  author = db.Column(db.String(64), index=True)
  body = db.column(db.String(1000))
  
  def __repr__(self):
    return '<Post %r>' % (self.id)

class Comment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  author = db.Column(db.String(64), index=True)
  body = db.Column(db.String(250))
  post = db.Column(db.Integer, db.ForeignKey('post.id'))

  def __repr__(self):
    return '<Comment %r>' % (self.id)

class Survey(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  post = db.Column(db.Integer, db.ForeignKey('post.id'))
  questions = db.relationship('Question', backref='parentsurvey', lazy='dynamic')

  def __repr__(self):
    return '<Survey %r>' % (self.id)

class Question(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String(500))
  answers = db.relationship('Answer', backref='parentquestion', lazy='dynamic')
  survey = db.Column(db.Integer, db.ForeignKey('survey.id'))

  def __repr__(self):
    return '<Survey %r>' % (self.id)

class Answer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String(500))
  question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

  def __repr__(self):
    return '<Survey %r>' % (self.id)
