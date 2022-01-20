import warnings
from WEB import *
from WEB.help_funcs import *


@app.route("/Usr/<_id>", methods=["GET", "POST"])
def student_home(_id):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if session["id"] == _id:
        return render_template("student/home.html")
