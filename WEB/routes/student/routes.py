import warnings

import pandas as pd

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
        enrolled_courses = list(
            pd.DataFrame(
                requests.get(
                    "http://127.0.0.1:5000/api/azure/sql",
                    {
                        "Type":
                        "Select",
                        "Query":
                        f"SELECT * FROM [Enrolled] WHERE [Student Id]={_id}",
                    },
                ).json()["message"],
                columns=[
                    "id",
                    "student_id",
                    "course_id",
                    "tutor_id",
                    "current_lesson",
                    "total_lesson",
                    "paid",
                ],
            )["course_id"])
        print(enrolled_courses)
        return render_template(
            "student/subject.html",
            courses=new_courses,
            _id=_id,
            enrolled_courses=enrolled_courses,
        )


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
                "Query": f"SELECT * FROM Courses WHERE [ID]={name_of_subject}",
            },
        )
        courses = courses.json()["message"][0]
        id_courses = courses[0]
        id_tutor = courses[-1]
        id_student = _id
        courses_content = eval(
            requests.get(
                "http://127.0.0.1:5000/api/azure/storage",
                {
                    "Container Name": "cource",
                    "file_name": f"{id_courses}-info.txt",
                    "Type": "Download File",
                },
            ).json()["message"])
        requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Type":
                "Insert",
                "Query":
                f"INSERT INTO [Enrolled]( [Student Id],[Course Id], [Tutor Id], [Current Lesson], [Total Lesson], [Paid] ) VALUES ({id_student}, {id_courses}, {id_tutor}, 0, {len(courses_content.keys())}, 'False')",
            },
        )
        return redirect(f"/Usr/{_id}/Subject/{name_of_subject}/")


@app.route("/Usr/<_id>/Subject/<name_of_subject>/Login",
           methods=["GET", "POST"])
@app.route("/Usr/<_id>/Subject/<name_of_subject>/Login/",
           methods=["GET", "POST"])
def student_subject_login(_id, name_of_subject):
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
                "Query": f"SELECT * FROM Courses WHERE [ID]={name_of_subject}",
            },
        )
        courses = courses.json()["message"][0]
        id_courses = courses[0]
        id_tutor = courses[-1]
        id_student = _id
        tutor = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Type": "Select",
                "Query": f"SELECT * FROM Tutor WHERE [ID]={id_tutor}"
            },
        ).json()["message"]
        courses = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Type": "Select",
                "Query": f"SELECT * FROM Courses WHERE [ID]={id_courses}",
            },
        ).json()["message"]
        student = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Type": "Select",
                "Query": f"SELECT * FROM Accounts WHERE [ID]={id_student}",
            },
        ).json()["message"]
        print(tutor, courses, student)
        return render_template(
            "student/enrolled_courses.html",
            _id=_id,
            courses=courses[0],
            tutor=tutor[0],
            student=student[0],
        )
