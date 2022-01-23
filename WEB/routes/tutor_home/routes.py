import warnings

from WEB import *
from WEB.help_funcs import *


@app.route("/Tutor/", methods=["GET", "POST"])
@app.route("/Tutor", methods=["GET", "POST"])
def home_tutor():
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    password = "01x2253x6871"
    config = requests.get("http://127.0.0.1:5000/api/get_config",
                          {"password": password})
    config = config.json()
    return render_template(
        "tutor_home/home.html",
        session=session,
    )


@app.route("/Tutor/Sign/Up", methods=["GET", "POST"])
@app.route("/Tutor/Sign/Up", methods=["GET", "POST"])
def home_tutor_sign_up():
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    password = "01x2253x6871"
    config = requests.get("http://127.0.0.1:5000/api/get_config",
                          {"password": password})
    config = config.json()
    if request.method == "POST":
        print("grwegrwe")
        email = request.form["Email"]
        password = request.form["Password"]
        user_name = request.form["User Name"]
        description = request.form["description"]
        qualification = request.form["qualification"]
        profile_picture = request.form["profile_picture"]
        full_name = request.form["Full Name"]
        contact_number = request.form["Contact Number"]
        # remember_password = request.form["Remember Password"]
        remember_password = ""
        if hp.validate_email(email) is False:
            flash("Invalid Email", "danger")
            return redirect("/Tutor/Sign/Up")
        already_accounts = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Query": "SELECT * FROM Tutor",
                "Type": "Select"
            },
        )
        already_accounts = already_accounts.json()
        for already_account in already_accounts["message"]:
            if already_account[1] == email and already_account[3] == hp.encode(
                    password):
                flash("Email is already exist.", "danger")
                return redirect("/Tutor/Sign/Up")
            if already_account[2] == user_name and already_account[
                    3] == hp.encode(password):
                flash("User Name is already exist.", "danger")
                return redirect("/Tutor/Sign/Up")
        session["2_Fac_Auth_Info"] = {
            "email": email,
            "user_name": user_name,
            "password": password,
            "remember_password": remember_password,
            "description": description,
            "qualification": qualification,
            "profile_picture": profile_picture,
            "full_name": full_name,
            "contact_number": contact_number,
        }
        session["2FACAUTH"] = True
        return redirect("/Tutor/2/Fac/Auth/")
    return render_template("tutor_home/sign_up.html",
                           session=session,
                           config=config)


@app.route("/Tutor/Sign/In", methods=["GET", "POST"])
@app.route("/Tutor/Sign/In/", methods=["GET", "POST"])
def home_tutor_sign_in():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    password = "01x2253x6871"
    config = requests.get("http://127.0.0.1:5000/api/get_config",
                          {"password": password})
    config = config.json()
    if request.method == "POST":
        user_name_or_email = request.form["Email or User Name"]
        password = request.form["Password"]
        remember_password = ""  # request.form["Remember Password"]
        already_accounts = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {
                "Query": "SELECT * FROM Tutor",
                "Type": "Select"
            },
        )
        already_accounts = already_accounts.json()
        ok = False
        for already_account in already_accounts["message"]:
            print(already_account[1], already_account[3])
            print(already_account[2])
            if already_account[1] == user_name_or_email and already_account[
                    2] == hp.encode(password):
                email = already_account[1]
                user_name = already_account[3]
                _id = already_account[0]
                rank = already_account[9]
                enabled = already_account[10]
                contact_number = already_account[8]
                full_name = already_account[7]
                profile_picture = already_account[6]
                qualification = already_account[5]
                description = already_account[4]
                ok = True
                print(
                    enabled,
                    contact_number,
                    full_name,
                    profile_picture,
                    qualification,
                    description,
                )
            elif already_account[3] == user_name_or_email and already_account[
                    2] == hp.encode(password):
                email = already_account[1]
                user_name = already_account[3]
                _id = already_account[0]
                rank = already_account[9]
                enabled = already_account[10]
                contact_number = already_account[8]
                full_name = already_account[7]
                profile_picture = already_account[6]
                qualification = already_account[5]
                description = already_account[4]
                ok = True
                print(
                    enabled,
                    contact_number,
                    full_name,
                    profile_picture,
                    qualification,
                    description,
                )
        if ok is False:
            session["Email or User Name"] = user_name_or_email
            session["Password"] = password
            flash("Email or User Name and Password is wrong.", "danger")
            return redirect("/Tutor/Sign/In")
        if enabled == "False":
            flash(
                "Your Account is Not Enabled yet or Your account is disabled.",
                "danger")
            return redirect("/Tutor/Sign/In")
        session["2_Fac_Auth_Info"] = {
            "email": email,
            "user_name": user_name,
            "_id": _id,
            "rank": rank,
            "password": password,
            "remember_password": remember_password,
            "enabled": enabled,
            "contact_number": contact_number,
            "full_name": full_name,
            "profile_picture": profile_picture,
            "qualification": qualification,
            "description": description,
        }
        session["2FACAUTH"] = False
        return redirect("/Tutor/2/Fac/Auth/")
    return render_template("tutor_home/sign_in.html",
                           session=session,
                           config=config)


@app.route("/Tutor/2/Fac/Auth/", methods=["POST", "GET"])
@app.route("/Tutor/2/Fac/Auth", methods=["POST", "GET"])
def tutor_two_factor_authentication():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    # try:
    if "2FACAUTH" in session:
        db = cluster["2FACAUTH"]
        collection = db["2FACAUTH"]
        if request.method == "POST":
            email_code = request.form["email"]
            contact_number_code = request.form["phone_number"]
            # results = [
            #     collection.find_one(
            #         {
            #             str(session["2_Fac_Auth_Info"]["email"]): str(email_code),
            #             str("94766428783"): str(contact_number_code),
            #             "user_name": session["2_Fac_Auth_Info"]["user_name"],
            #         }
            #     )
            # ]
            results = ["A", "B"]  # TODO
            if results == [None]:
                flash("Email or Phone Number code is wrong.", "danger")
                return redirect("/Tutor/Sign/In")
            # collection.delete_one(results[0])
            if session["2FACAUTH"] is False:
                email = session["2_Fac_Auth_Info"]["email"]
                user_name = session["2_Fac_Auth_Info"]["user_name"]
                _id = session["2_Fac_Auth_Info"]["_id"]
                rank = session["2_Fac_Auth_Info"]["rank"]
                password = session["2_Fac_Auth_Info"]["password"]
                remember_password = session["2_Fac_Auth_Info"][
                    "remember_password"]
                enabled = session["2_Fac_Auth_Info"]["enabled"]
                contact_number = session["2_Fac_Auth_Info"]["contact_number"]
                full_name = session["2_Fac_Auth_Info"]["full_name"]
                profile_picture = session["2_Fac_Auth_Info"]["profile_picture"]
                qualification = session["2_Fac_Auth_Info"]["qualification"]
                description = session["2_Fac_Auth_Info"]["description"]
                session["id"] = _id
                session["User Name"] = user_name
                session["Email"] = email
                session["Password"] = password
                session["Rank"] = rank
                session["Remember Password"] = remember_password
                session["Enabled"] = enabled
                session["Phone Number"] = contact_number
                session["Full Name"] = full_name
                session["Profile Picture"] = profile_picture
                session["Qualification"] = qualification
                session["Description"] = description
                session["Is_Tutor"] = True
                session.pop("2FACAUTH")
                session.pop("2_Fac_Auth_Info")
                if remember_password == "on":
                    session.permanent = True
                flash("You have loged in successfully", "success")
                return redirect(f"/Tutor/{_id}/")
            else:
                email = session["2_Fac_Auth_Info"]["email"]
                user_name = session["2_Fac_Auth_Info"]["user_name"]
                password = session["2_Fac_Auth_Info"]["password"]
                remember_password = session["2_Fac_Auth_Info"][
                    "remember_password"]
                description = session["2_Fac_Auth_Info"]["description"]
                qualification = session["2_Fac_Auth_Info"]["qualification"]
                profile_picture = session["2_Fac_Auth_Info"]["profile_picture"]
                full_name = session["2_Fac_Auth_Info"]["full_name"]
                contact_number = session["2_Fac_Auth_Info"]["contact_number"]
                already_accounts = requests.get(
                    "http://127.0.0.1:5000/api/azure/sql",
                    {
                        "Query": f"""
                        INSERT INTO
                            [Tutor] ([Email],[Password],[User_Name],[Description],[Qualification],[Profile Picture],[Full Name],[Contact Number],[Rating],[Enabled])
                        VALUES
                            (
                                '{email}','{hp.encode(password)}','{user_name}','{description}','{qualification}','{profile_picture}','{full_name}','{contact_number}','1','False'
                            );
                        """,
                        "Type": "Insert",
                    },
                )
                already_accounts = already_accounts.json()
                session["Email or User Name"] = user_name
                session["Password"] = password
                flash("You will be validated as soon as possible", "success")
                return redirect("/Tutor/Sign/In")
        print(session["2_Fac_Auth_Info"])
        hf = Help_Funcs()
        hf.two_fac_auth(
            session["2_Fac_Auth_Info"]["user_name"],
            session["2_Fac_Auth_Info"]["email"],
            session["2_Fac_Auth_Info"]["contact_number"],
        )  # TODO
        return render_template("/tutor_home/2_fac_auth.html")
