"""Data model"""

from . import db, mm
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(100))
    posts=db.relationship('Post', backref='user', lazy=True)
    def __repr__(self):
        return f"User('{self.name}','{self.email}', '{self.password}')"


class Post(db.Model):
    __tablename__ = "post"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)
    author_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.id}', '{self.title}', '{self.content}', '{self.pub_date}', '{self.author_id}'"

class Events(db.Model):
    __tablename__ = "events"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    organizer = db.Column(db.String)
    event_date = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"Events('{self.id}', '{self.title}', '{self.organizer}', '{self.event_date}'"




class UserSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session

class PostSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        sqla_session = db.session
