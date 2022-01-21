import warnings

from WEB import *
from WEB.help_funcs import *


@app.route("/Usr/<_id>", methods=["GET", "POST"])
@app.route("/Usr/<_id>/", methods=["GET", "POST"])
def student_home(_id):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if str(session["id"]) == str(_id):
        subjects = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Type": "Select",
                "Query": f"SELECT * FROM Subjects"
            },
        )
        subjects = subjects.json()["message"]
        iter_list = []
        new_subjects = []
        idx = 0
        for subject in subjects:
            if idx % 3 == 0:
                new_subjects.append(iter_list)
                iter_list = []
            iter_list.append(subject)
            idx += 1
        new_subjects.append(iter_list)
        return render_template("student/home.html",
                               subjects=new_subjects,
                               session=session,
                               _id=_id)


@app.route("/Usr/<_id>/Subject/<name_of_subject>/", methods=["GET", "POST"])
@app.route("/Usr/<_id>/Subject/<name_of_subject>", methods=["GET", "POST"])
def student_subjects(_id, name_of_subject):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if str(session["id"]) == str(_id):
        courses = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Type": "Select",
                "Query":
                f"SELECT * FROM Courses WHERE Subject={name_of_subject}",
            },
        )
        courses = courses.json()["message"]
        iter_list = []
        new_courses = []
        idx = 0
        for course in courses:
            if idx % 3 == 0:
                new_courses.append(iter_list)
                iter_list = []
            iter_list.append(course)
            idx += 1
        new_courses.append(iter_list)
        return render_template("student/subject.html",
                               courses=new_courses,
                               _id=_id)


@app.route("/Usr/<_id>/Subject/<name_of_subject>/Enroll",
           methods=["GET", "POST"])
@app.route("/Usr/<_id>/Subject/<name_of_subject>/Enroll/",
           methods=["GET", "POST"])
def student_subject_enroll(_id, name_of_subject):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if str(session["id"]) == str(_id):
        courses = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Type": "Select",
                "Query":
                f"SELECT * FROM Courses WHERE Subject={name_of_subject}",
            },
        )
        courses = courses.json()["message"]
        iter_list = []
        new_courses = []
        idx = 0
        for course in courses:
            if idx % 3 == 0:
                new_courses.append(iter_list)
                iter_list = []
            iter_list.append(course)
            idx += 1
        new_courses.append(iter_list)
        return render_template("student/subject.html", courses=new_courses)
