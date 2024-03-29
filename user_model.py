from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String(50))
    full_name = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password= db.Column(db.String(100),nullable=False)
    submitted_by=db.Column(db.String(100))
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow )


    def to_dict(self):
        return {
            'id': self.id,
            'type':self.type,
            'full_name':self.full_name,
            'username': self.username,
            'email': self.email,
            'password':self.password,
            'submitted_by':self.submitted_by,
            'updated_at':self.updated_at
        }

class Course(db.Model):
    __tablename__='courses'