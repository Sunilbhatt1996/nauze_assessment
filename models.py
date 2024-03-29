from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db, ma
db = SQLAlchemy()

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50))
    submitted_by=db.Column(db.String(100))
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow )


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String(50))
    full_name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password= db.Column(db.String(100),nullable=False)
    submitted_by=db.Column(db.String(100))
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow )

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

user_schema = UserSchema()
users_schema = UserSchema(many=True)
    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'type':self.type,
    #         'full_name':self.full_name,
    #         'username': self.username,
    #         'email': self.email,
    #         'password':self.password,
    #         'submitted_by':self.submitted_by,
    #         'updated_at':self.updated_at
    #     }

class Course(db.Model):
    __tablename__='courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name=db.Column(db.String(50))
    full_name = db.Column(db.String(50))
    department_id = db.relationship(
        Department,
        backref="department",
        cascade="all, delete, delete-orphan",
        single_parent=True
    )
    semester = db.Column(db.Integer)
    classes = db.Column(db.String(50))
    lecture_hours = db.Column(db.Integer)
    submitted_by=db.Column(db.String(100))
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow )


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        load_instance = True
        sqla_session = db.session

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    department_id = db.relationship(
        Department,
        backref="department",
        cascade="all, delete, delete-orphan",
        single_parent=True
    )
    classes = db.Column(db.String(50))
    submitted_by=db.Column(db.String(100))
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow )

class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True
        sqla_session = db.session

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        load_instance = True
        sqla_session = db.session

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)

class Attendance(db.Model):
    __tablename__ = 'attendance_log'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    course_id = db.relationship(
        Course,
        backref="course",
        cascade="all, delete, delete-orphan",
        single_parent=True
    )
    present = db.Column(db.String(50))
    submitted_by=db.Column(db.String(100))
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow )

class AttendanceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Attendance
        load_instance = True
        sqla_session = db.session

attendance_schema = AttendanceSchema()
Attendances_schema = AttendanceSchema(many=True)