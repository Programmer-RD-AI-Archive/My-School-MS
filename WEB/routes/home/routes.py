import warnings

from WEB import *
from WEB.help_funcs import *


@app.route("/", methods=["GET", "POST"])
def home():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if request.method == "POST":
        email = request.form["email"]
        question = request.form["Question"]
        already_accounts = requests.get("http://127.0.0.1:5000/api/Accounts", )
        already_accounts = already_accounts.json()
        ok = None
        for already_account in already_accounts["message"]:
            if (already_account[2] == email
                    and already_account[4] == hp.encode(question)
                    and already_account[1] == 5):
                ok = True
                password = already_account[4]
                email = already_account[2]
                user_name = already_account[3]
                rank = already_account[1]
                _id = already_account[0]
            elif (already_account[3] == email
                  and already_account[4] == hp.encode(question)
                  and already_account[1] == 5):
                ok = True
                password = already_account[4]
                email = already_account[2]
                user_name = already_account[3]
                rank = already_account[1]
                _id = already_account[0]
        if ok is True:
            session["Is_Admin"] = True
            session["id"] = _id
            session["User Name"] = user_name
            session["Email"] = email
            session["Rank"] = rank
            session["Password"] = password
            return redirect("/Admin/")
        config = requests.post(
            "http://127.0.0.1:5000/api/Contact_Us",
            {
                "email": email,
                "question": question
            },
        )
        config = config.json()
        if config["message"] is True:
            try:
                session.pop("email")
                session.pop("question")
            except Exception as e:
                warnings.filterwarnings(e)
            flash(
                "Your Question will be answered as soon as possible by our team.",
                "success",
            )
            return redirect("/")
        session["email"] = email
        session["question"] = question
        flash("There is some error so please try again.", "danger")
        return redirect("/")
    password = "01x2253x6871"
    config = requests.get("http://127.0.0.1:5000/api/get_config",
                          {"password": password})
    config = config.json()
    return render_template(
        "home/home.html",
        gif_1=config["config"]["Home"]["Help you Learn Stuff"]["Gif"],
        gif_2=config["config"]["Home"]["About Us"]["Gif"],
        gif_3=config["config"]["Home"]["Contact Us"]["Gif"],
        description_1=config["config"]["Home"]["Help you Learn Stuff"]
        ["Description"],
        description_2=config["config"]["Home"]["About Us"]["Description"],
        description_3=config["config"]["Home"]["Contact Us"]["Description"],
        session=session,
    )


@app.route("/Sign/Up", methods=["GET", "POST"])
@app.route("/Sign/Up/", methods=["GET", "POST"])
def sign_up():
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
        email = request.form["Email"]
        password = request.form["Password"]
        user_name = request.form["User Name"]
        if hp.validate_email(email) is False:
            flash("Invalid Email", "danger")
            return redirect("/Sign/Up")
        already_accounts = requests.get("http://127.0.0.1:5000/api/Accounts", )
        already_accounts = already_accounts.json()
        for already_account in already_accounts["message"]:
            if already_account[1] == email and already_account[3] == hp.encode(
                    password):
                flash("Email is already exist.", "danger")
                return redirect("/Sign/Up")
            if already_account[2] == user_name and already_account[
                    3] == hp.encode(password):
                flash("User Name is already exist.", "danger")
                return redirect("/Sign/Up")

        session["2_Fac_Auth_Info"] = {
            "email": email,
            "user_name": user_name,
            "password": password,
        }
        session["2FACAUTH"] = True
        return redirect("/2/Fac/Auth/")

    return render_template("home/sign_up.html", session=session, config=config)


@app.route("/Sign/In", methods=["GET", "POST"])
@app.route("/Sign/In/", methods=["GET", "POST"])
def sign_in():
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
        already_accounts = requests.get("http://127.0.0.1:5000/api/Accounts", )
        already_accounts = already_accounts.json()
        ok = None
        for already_account in already_accounts["message"]:
            if already_account[2] == user_name_or_email and already_account[
                    4] == hp.encode(password):
                email = already_account[2]
                user_name = already_account[3]
                _id = already_account[0]
                rank = already_account[1]
                ok = True
            elif already_account[3] == user_name_or_email and already_account[
                    4] == hp.encode(password):
                email = already_account[2]
                user_name = already_account[3]
                _id = already_account[0]
                rank = already_account[1]
                ok = True
        if ok is False:
            session["Email or User Name"] = user_name_or_email
            session["Password"] = password
            flash("Email or User Name and Password is wrong.", "danger")
            return redirect("/Sign/In")
        session["2_Fac_Auth_Info"] = {
            "email": email,
            "user_name": user_name,
            "_id": _id,
            "rank": rank,
            "password": password,
        }
        session["2FACAUTH"] = False
        return redirect("/2/Fac/Auth/")
    return render_template("home/sign_in.html", session=session, config=config)


@app.route("/2/Fac/Auth/", methods=["POST", "GET"])
@app.route("/2/Fac/Auth", methods=["POST", "GET"])
def sign_two_face_auth():
    # try:
    if "2FACAUTH" in session:
        db = cluster["2FACAUTH"]
        collection = db["2FACAUTH"]
        if request.method == "POST":
            email_code = request.form["email"]
            phone_number_code = request.form["phone_number"]
            # results = [
            #     collection.find_one(
            #         {
            #             str(session["2_Fac_Auth_Info"]["email"]): str(email_code),
            #             str("94766428783"): str(phone_number_code),
            #             "user_name": session["2_Fac_Auth_Info"]["user_name"],
            #         }
            #     )
            # ]
            results = ["A", "B"]  # TODO
            if results == [None]:
                flash("Email or Phone Number code is wrong.", "danger")
                return redirect("/Sign/In")
            # collection.delete_one(results[0])
            if session["2FACAUTH"] is False:
                email = session["2_Fac_Auth_Info"]["email"]
                user_name = session["2_Fac_Auth_Info"]["user_name"]
                _id = session["2_Fac_Auth_Info"]["_id"]
                rank = session["2_Fac_Auth_Info"]["rank"]
                password = session["2_Fac_Auth_Info"]["password"]
                session["id"] = _id
                session["User Name"] = user_name
                session["Email"] = email
                session["Password"] = password
                session["Rank"] = rank
                session.pop("2FACAUTH")
                session.pop("2_Fac_Auth_Info")
                flash("You have loged in successfully", "success")
                return redirect(f"/Usr/{_id}/")
            else:
                pass
        hf = Help_Funcs()
        hf.two_fac_auth(
            session["2_Fac_Auth_Info"]["user_name"],
            session["2_Fac_Auth_Info"]["email"],
            "94766428783",
        )  # TODO
        return render_template("/home/2_fac_auth.html")


@app.route("/payment_methods", methods=["POST", "GET"])
@app.route("/payment_methods/", methods=["POST", "GET"])
def payment_methods():
    try:
        url_success = "http://127.0.0.1:5000/payment_methods_success/"
        url_decline = "http://127.0.0.1:5000/payment_methods_decline"
        if "payment_methods" in session:
            if request.method == "POST":
                coupon = request.form["Coupon"]
                session["Coupon"] = coupon
                flash("OK Coupon Added", "success")
                return redirect("/payment_methods")
            try:
                session_subscription = stripe.checkout.Session.create(
                    payment_method_types=["card"],
                    line_items=[{
                        "price": "price_1JIoxDJzMECqGOD83XVcIgop",
                        "quantity": 1,
                    }],
                    mode="subscription",
                    success_url=url_success,
                    cancel_url=url_decline,
                    discounts=[{
                        "coupon": session["Coupon"],
                    }],
                )
            except:
                #
                session_subscription = stripe.checkout.Session.create(
                    payment_method_types=["card"],
                    line_items=[{
                        "price": "price_1JIoxDJzMECqGOD83XVcIgop",
                        "quantity": 1,
                    }],
                    mode="subscription",
                    success_url=url_success,
                    cancel_url=url_decline,
                )
            session["Subscription"] = session_subscription
            return render_template(
                "/home/payment_methods.html",
                checkout_session_id_subscription=session_subscription["id"],
                checkout_public_key=app.config["STRIPE_PUBLIC_KEY"],
            )
    except:
        return abort(500)


@app.route("/payment_methods_success/")
@app.route("/payment_methods_success")
def payment_methods_success():
    payment_id_info = session["Subscription"]
    if "payment_methods" in session:
        if "Coupon" in session:
            session.pop("Coupon")
        session.pop("payment_methods")
        password = session["2_Fac_Auth_Info"]["password"]
        email = session["2_Fac_Auth_Info"]["email"]
        user_name = session["2_Fac_Auth_Info"]["user_name"]
        account_add = requests.post(
            "http://127.0.0.1:5000/api/Accounts",
            {
                "email": email,
                "password": hp.encode(password),
                "user_name": user_name,
            },
        )
        account_add = account_add.json()
        session["Email or User Name"] = email
        session["Password"] = password
        session.pop("payment_methods")
        session.pop("Subscription")
        flash("Your account has been created.", "success")
        flash(
            "Payment Went Through!",
            "success",
        )
        return redirect("/")


@app.route("/payment_methods_decline/")
@app.route("/payment_methods_decline")
def payment_methods_decline():
    try:
        if "payment_methods" in session:
            flash("Payment Didnt Go Through! \n Try again please.", "success")
            return redirect("/payment_methods")
    except:
        return abort(500)
