from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    author = db.Column(db.String(64))
    body = db.Column(db.String(140))
    questions = db.Relationship('Question', backref='post', lazy='dynamic')
    comments = db.Relationship('Comment', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Post %r>' % (self.body)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(1))
    body = db.Column(db.String(500))
    answers = db.Relationship('Answer', backref='question', lazy='dynamic')    

    def __repr__(self):
        return '<Question %r>' % (self.body)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    response_id = db.Column(db.Integer, db.ForeignKey('response.id'))
    type = db.Column(db.String(1))
    body = db.Column(db.String(500))
    
    def __repr__(self):
        return '<Answer %r>' % (self.body)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    author = db.Column(db.String(64)
    answers = db.Relationship('Answer', backref='set', lazy='dynamic')

    def __repr__(self):
        return '<Response %r>' % (self.id)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    author = db.Column(db.String(64))
    body = db.Column(db.String(500))

    def __repr__(self):
        return '<Comment %r>' % (self.body)
