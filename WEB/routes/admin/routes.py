import warnings

from WEB import *
from WEB.help_funcs import *


@app.route("/Admin/")
@app.route("/Admin")
def admin_home():
    if "Is_Admin" in session:
        return render_template("admin/home.html", session=session)


@app.route("/Admin/Tutors")
@app.route("/Admin/Tutors/")
def admin_tutors():
    if "Is_Admin" in session:
        already_accounts = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": "SELECT * FROM Tutor", "Type": "Select"},
        )
        already_accounts = already_accounts.json()["message"]
        return render_template("admin/tutors.html", tutors=already_accounts)


@app.route("/Admin/Tutors/Enable/<_id>")
@app.route("/Admin/Tutors/Enable/<_id>/")
def admin_tutors_enable(_id):
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


@app.route("/Admin/Tutors/Disable/<_id>")
@app.route("/Admin/Tutors/Disable/<_id>/")
def admin_tutors_disable(_id):
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


@app.route("/Admin/Accounts")
@app.route("/Admin/Accounts/")
def admin_accounts():
    if "Is_Admin" in session:
        accounts = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Type": "Select", "Query": "SELECT * FROM Accounts"},
        )
        accounts = accounts.json()["message"]
        return render_template("admin/accounts.html", accounts=accounts)


@app.route("/Admin/Accounts/Edit/<_id>")
@app.route("/Admin/Accounts/Edit/<_id>/")
def admin_account_edit():
    if "Is_Admin" in session:
        # accounts = requests.get(
        #     "http://127.0.0.1:5000/api/azure/sql",
        #     {"Type": "Select", "Query": "SELECT * FROM Accounts"},
        # )
        # accounts = accounts.json()["message"]
        flash("Not Working TODO", "success")  # TODO
        return redirect("/Admin/Accounts")


@app.route("/Admin/Accounts/Delete/<_id>")
@app.route("/Admin/Accounts/Delete/<_id>/")
def admin_account_delete(_id):
    if "Is_Admin" in session:
        accounts = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Type": "Insert", "Query": f"DELETE FROM Accounts WHERE ID={_id}; "},
        )
        accounts = accounts.json()["message"]
        flash("Deleted", "success")
        return redirect("/Admin/Accounts")


@app.route("/Admin/Subjects", methods=["GET", "POST"])
@app.route("/Admin/Subjects/", methods=["GET", "POST"])
def admin_subjects():
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


@app.route("/Admin/Subjects/Delete/<_id>", methods=["GET", "POST"])
@app.route("/Admin/Subjects/Delete/<_id>/", methods=["GET", "POST"])
def admin_subject_delete(_id):
    if "Is_Admin" in session:
        subjects = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Type": "Insert", "Query": f"DELETE FROM Subjects WHERE ID={_id}; "},
        )
        subjects = subjects.json()["message"]
        flash("Deleted", "success")
        return redirect("/Admin/Subjects")


@app.route("/Admin/Subjects/Edit/<_id>/")
@app.route("/Admin/Subjects/Edit/<_id>/")
def admin_subject_edit(_id):
    if "Is_Admin" in session:
        # accounts = requests.get(
        #     "http://127.0.0.1:5000/api/azure/sql",
        #     {"Type": "Select", "Query": "SELECT * FROM Accounts"},
        # )
        # accounts = accounts.json()["message"]
        flash("Not Working TODO", "success")  # TODO
        return redirect("/Admin/Subjects")


@app.route("/Admin/Log/Out")
@app.route("/Admin/Log/Out/")
def admin_log_out():
    if "Is_Admin" in session:
        session.pop("Is_Admin")
        session.pop("id")
        session.pop("User Name")
        session.pop("Email")
        session.pop("Rank")
        session.pop("Password")
        flash("Loged Out", "success")
        return redirect("/")
