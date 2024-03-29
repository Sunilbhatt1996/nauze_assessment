# app.py

from flask import Flask,render_template,request,jsonify # Remove: import Flask
# import connexion
import query,models

app = Flask(__name__)

# app = connexion.App(__name__, specification_dir="./")
# app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/create_user', methods=['POST'])
def create_course():
    request_data=models.User.load(request.get_json())
    output=query.create_user(request_data)
    return jsonify(output)

@app.route('/all-user', methods=['POST'])
def all_user():
    output=query.user_read_all()
    return jsonify(output)

@app.route('/find_course', methods=['GET'])
def find_course():
    request_data=models.Course.load(request.get_json())
    output=query.find_course(request_data)
    return jsonify(output)

@app.route('/all-course', methods=['POST'])
def all_course():
    output=query.course_read_all()
    return jsonify(output)

@app.route('/create_course', methods=['POST'])
def create_course():
    request_data=models.Course.load(request.get_json())
    output=query.create_course(request_data)
    return jsonify(output)

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    request_data=models.Attendance.load(request.get_json())
    output=query.mark_attendance(request_data)
    return jsonify(output)

@app.route('/create_department', methods=['POST'])
def create_dept():
    request_data=models.Department.load(request.get_json())
    output=query.create_department(request_data)
    return jsonify(output)

@app.route('/all-department', methods=['POST'])
def all_dept():
    output=query.department_read_all()
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)