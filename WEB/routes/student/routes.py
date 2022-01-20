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
            {"Type": "Select", "Query": f"SELECT * FROM Subjects"},
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
        return render_template("student/home.html", subjects=new_subjects)
    return "zgdrghdr"
