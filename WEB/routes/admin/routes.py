import warnings

from WEB import *
from WEB.help_funcs import *


@app.route("/Admin/")
@app.route("/Admin")
def admin_home():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        return render_template("admin/home.html", session=session)
    return abort(404)


@app.route("/Admin/Tutors")
@app.route("/Admin/Tutors/")
def admin_tutors():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        already_accounts = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": "SELECT * FROM Tutor", "Type": "Select"},
        )
        already_accounts = already_accounts.json()["message"]
        return render_template("admin/tutors.html", tutors=already_accounts)
    return abort(404)


@app.route("/Admin/Tutors/Enable/<_id>")
@app.route("/Admin/Tutors/Enable/<_id>/")
def admin_tutors_enable(_id):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        email = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": f"SELECT * FROM Tutor WHERE ID={_id}", "Type": "Select"},
        ).json()["message"][0][1]
        print(email)
        hp = Help_Funcs()
        hp.send_email(
            "Your My School Account is Enabled !",
            email,
            "Your My School Account is Enabled ! Go to MySchool and login to your tutor account. \n Congratz. \n Best of Luck",
        )
        requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Type": "Insert",
                "Query": f"""
                UPDATE Tutor
                SET Enabled = 'True'
                WHERE ID={_id};
            """,
            },
        )
        flash("Enabled", "success")
        return redirect("/Admin/Tutors")
    return abort(404)


@app.route("/Admin/Tutors/Disable/<_id>")
@app.route("/Admin/Tutors/Disable/<_id>/")
def admin_tutors_disable(_id):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        email = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": f"SELECT * FROM Tutor WHERE ID={_id}", "Type": "Select"},
        ).json()["message"][0][1]
        print(email)
        hp = Help_Funcs()
        hp.send_email(
            "Your My School Account is Disabled !",
            email,
            "Your My School Account is Disabled ! Go to MySchool and login to your tutor account.",
        )
        requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Type": "Insert",
                "Query": f"""
                UPDATE Tutor
                SET Enabled = 'False'
                WHERE ID={_id};
            """,
            },
        )
        flash("Disabled", "success")
        return redirect("/Admin/Tutors")
    return abort(404)


@app.route("/Admin/Accounts")
@app.route("/Admin/Accounts/")
def admin_accounts():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        accounts = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Type": "Select", "Query": "SELECT * FROM Accounts"},
        )
        accounts = accounts.json()["message"]
        return render_template("admin/accounts.html", accounts=accounts)
    return abort(404)


@app.route("/Admin/Accounts/Edit/<_id>")
@app.route("/Admin/Accounts/Edit/<_id>/")
def admin_account_edit():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        # accounts = requests.get(
        #     "http://127.0.0.1:5000/api/azure/sql",
        #     {"Type": "Select", "Query": "SELECT * FROM Accounts"},
        # )
        # accounts = accounts.json()["message"]
        flash("Not Working TODO", "success")  # TODO
        return redirect("/Admin/Accounts")
    return abort(404)


@app.route("/Admin/Accounts/Delete/<_id>")
@app.route("/Admin/Accounts/Delete/<_id>/")
def admin_account_delete(_id):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        accounts = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Type": "Insert", "Query": f"DELETE FROM Accounts WHERE ID={_id}; "},
        )
        accounts = accounts.json()["message"]
        flash("Deleted", "success")
        return redirect("/Admin/Accounts")
    return abort(404)


@app.route("/Admin/Subjects", methods=["GET", "POST"])
@app.route("/Admin/Subjects/", methods=["GET", "POST"])
def admin_subjects():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        if request.method == "POST":
            name = request.form["Name"]
            description = request.form["Description"]
            link = request.form["Link"]
            subjects = requests.get(
                "http://127.0.0.1:5000/api/azure/sql",
                {
                    "Type": "Insert",
                    "Query": f"""
                INSERT INTO
                    [Subjects] ([Name],[Description],[Image])
                VALUES
                    (
                       '{name}','{description}','{link}'
                    );
                """,
                },
            )
            subjects = subjects.json()["message"]
        subjects = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Type": "Select", "Query": f"SELECT * FROM Subjects"},
        )
        subjects = subjects.json()["message"]
        return render_template("/admin/subjects.html", subjects=subjects)
    return abort(404)


@app.route("/Admin/Subjects/Delete/<_id>", methods=["GET", "POST"])
@app.route("/Admin/Subjects/Delete/<_id>/", methods=["GET", "POST"])
def admin_subject_delete(_id):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        subjects = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Type": "Insert", "Query": f"DELETE FROM Subjects WHERE ID={_id}; "},
        )
        subjects = subjects.json()["message"]
        flash("Deleted", "success")
        return redirect("/Admin/Subjects")
    return abort(404)


@app.route("/Admin/Subjects/Edit/<_id>/")
@app.route("/Admin/Subjects/Edit/<_id>/")
def admin_subject_edit(_id):
    if "Is_Admin" in session:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        # accounts = requests.get(
        #     "http://127.0.0.1:5000/api/azure/sql",
        #     {"Type": "Select", "Query": "SELECT * FROM Accounts"},
        # )
        # accounts = accounts.json()["message"]
        flash("Not Working TODO", "success")  # TODO
        return redirect("/Admin/Subjects")
    return abort(404)


@app.route("/Admin/Log/Out")
@app.route("/Admin/Log/Out/")
def admin_log_out():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Admin" in session:
        session.pop("Is_Admin")
        session.pop("id")
        session.pop("User Name")
        session.pop("Email")
        session.pop("Rank")
        session.pop("Password")
        flash("Loged Out", "success")
        return redirect("/")
    return abort(404)
