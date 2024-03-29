# people.py

from datetime import datetime
from flask import abort
import models
from config import db, ma

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def user_read_all():
    users=models.User.query.all()
    return models.users_schema.dump(users)
 
def find_user(user_list):
    uname = user_list.get("user_name")
    password =user_list.get("password")
    existing_person = models.User.query.filter(models.User.username == uname,
                                                models.User.password==password).one_or_none()
    if existing_person is not None:
        return models.user_schema.dump(existing_person),200
    else:
        return "Invalid Credential"
    

def create_user(user_list):
    uname = user_list.get("user_name")
    existing_person = models.User.query.filter(models.User.username == uname).one_or_none()

    if existing_person is None:
        new_user = models.user_schema.load(user_list, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return models.user_schema.dump(new_user), 201
    else:
        abort(406, f"User name is already exists")

def course_read_all():
    courses=models.Course.query.all()
    return models.courses_schema.dump(courses)

def find_course(id):
    course=models.Course.query.filter(models.Course.id==id).one_or_none()
    if course is not None:
        return models.course_schema.dump(course)
    else:
        abort(404, f"Course not found")

def create_course(course_list):
    uname = course_list.get("course_name")
    existing_person = models.Course.query.filter(models.Course.course_name == uname).one_or_none()

    if existing_person is None:
        new_course = models.course_schema.load(course_list, session=db.session)
        db.session.add(new_course)
        db.session.commit()
        return models.course_schema.dump(new_course), 201
    else:
        abort(406, f"User name is already exists")

def mark_attendance(data):
    s_data=models.Attendance.query.filter(models.Attendance.student_id==data.get('student_id')).one_or_none
    if s_data is  None:
        attend = models.attendance_schema.load(data, session=db.session)
        db.session.add(attend)
        db.session.commit()
        return models.attendance_schema.dump(attend), 201
    else:
        attend = models.attendance_schema.load(data, session=db.session)
        s_data.present = attend.present
        db.session.merge(s_data)
        db.session.commit()
        return models.attendance_schema.dump(s_data), 201



def create_department(dept_list):
    uname = dept_list.get("department_name")
    existing_person = models.Department.query.filter(models.Department.department_name == uname).one_or_none()

    if existing_person is None:
        new_dept = models.department_schema.load(dept_list, session=db.session)
        db.session.add(new_dept)
        db.session.commit()
        return models.department_schema.dump(new_dept), 201
    else:
        abort(406, f"User name is already exists")

def department_read_all():
    depts=models.Department.query.all()
    return models.departments_schema.dump(depts)
