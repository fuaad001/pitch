from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches = db.relationship("Pitch", backref= "user", lazy="dynamic")
    reviews = db.relationship("Review", backref = "user", lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'


class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(255))
    title = db.Column(db.String(255))
    pitch_statement = db.Column(db.VARCHAR())
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    vote_count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    Reviews = db.relationship("Review", backref = "pitch", lazy = "dynamic")

    def like(self):
        self.likes = self.likes + 1
        self.vote_count = self.likes - self.dislikes
        db.session.add(self)
        db.session.commit()

    def dislike(self):
        self.dislikes = self.dislikes + 1
        self.vote_count = self.likes - self.dislikes
        db.session.add(self)
        db.session.commit()

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def get_pitch_reviews(self):
        pitch = Pitch.query.filter_by(id = self.id).first()
        reviews = Review.query.filter_by(pitch_id = pitch.id).order_by(Review.posted.desc())
        return reviews



class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
    pitch_title = db.Column(db.String)
    pitch_review_title = db.Column(db.String)
    pitch_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls, id):
        reviews = Review.query.filter_by(pitch_id = id).all()
        return reviews
