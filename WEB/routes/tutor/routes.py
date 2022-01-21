from bs4 import *
import warnings
from WEB import *
from WEB.help_funcs import *

link_of_resource_dict = {1: "Video", 2: "Image", 3: "Sound", 4: "Website"}


@app.route("/Tutor/<_id>", methods=["GET", "POST"])
@app.route("/Tutor/<_id>/", methods=["GET", "POST"])
def tutor(_id):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return render_template("tutor/home.html", session=session, _id=_id)


@app.route("/Tutor/<_id>/Courses", methods=["GET", "POST"])
@app.route("/Tutor/<_id>/Courses/", methods=["GET", "POST"])
def tutor_courses(_id):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Tutor" in session:
        resources = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": "SELECT * FROM Resources", "Type": "Select"},
        ).json()["message"]
        questions = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": "SELECT * FROM Questions", "Type": "Select"},
        ).json()["message"]
        courses = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": "SELECT * FROM Courses", "Type": "Select"},
        ).json()["message"]
        new_cources = []
        iter_cources = []
        idx = 0
        for cource in courses:
            if idx % 2 == 0:
                new_cources.append(iter_cources)
                iter_cources = []
            idx += 1
            iter_cources.append(cource)
        new_cources.append(iter_cources)
        subjects = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": "SELECT * FROM Subjects", "Type": "Select"},
        ).json()["message"]
        return render_template(
            "tutor/courses.html",
            resources=resources,
            questions=questions,
            courses=new_cources,
            _id=_id,
            subjects=subjects,
        )
    return abort(404)


@app.route("/Tutor/<_id>/Courses/Post/", methods=["GET", "POST"])
@app.route("/Tutor/<_id>/Courses/Post", methods=["GET", "POST"])
def tutor_courses_post(_id):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Tutor" in session:
        request_forms = request.form
        request_forms = dict(request_forms)
        print(request_forms)
        new_request_forms = ""
        for key, val in zip(request_forms.keys(), request_forms.values()):
            new_request_forms += key
            new_request_forms += val
        request_forms = eval(new_request_forms)
        whole_content = request_forms["whole_content"]
        whole_content = BeautifulSoup(whole_content, "html.parser")
        info = request_forms["info"]
        image = request_forms["image"]
        name = request_forms["name"]
        marks = request_forms["marks"]
        description = request_forms["description"]
        subject = request_forms["subject"]
        response = requests.put(
            "http://127.0.0.1:5000/api/courses",
            {
                "whole_content": str(whole_content),
                "info": str(info),
                "image": str(image),
                "name": str(name),
                "marks": str(marks),
                "description": str(description),
                "subject": str(subject),
                "_id": str(_id),
            },
        ).json()
        flash("Cources added", "success")
        return redirect(f"/Tutor/{_id}/Courses")
    return abort(404)


@app.route("/Tutor/<_id>/Question", methods=["GET", "POST"])
@app.route("/Tutor/<_id>/Question/", methods=["GET", "POST"])
def tutor_question(_id):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Tutor" in session:
        returned_vals = requests.get("http://127.0.0.1:5000/api/questions").json()
        returned_vals = returned_vals["message"]
        return render_template(
            "tutor/question.html",
            config=config,
            session=session,
            questions=returned_vals,
            _id=_id,
        )
    return abort(404)


@app.route("/Tutor/<_id>/Resources", methods=["GET", "POST"])
@app.route("/Tutor/<_id>/Resources/", methods=["GET", "POST"])
def tutor_resources(_id):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Tutor" in session:
        if request.method == "POST":
            method_of_resource = request.form["method-of-resource"]
            link_of_resource = request.form["link-of-resource"]
            title = request.form["Title"]
            description = request.form["Description"]
            results = requests.put(
                "http://127.0.0.1:5000/api/resources",
                {
                    "method_of_resource": method_of_resource,
                    "link_of_resource": link_of_resource,
                    "title": title,
                    "description": description,
                },
            ).json()
            flash("Resource Added", "success")
            return redirect("/Tutor/Resources")
        results = requests.get(
            "http://127.0.0.1:5000/api/resources",
        ).json()
        return render_template(
            "tutor/resources.html",
            session=session,
            resources=results["message"],
            link_of_resource_dict=link_of_resource_dict,
            _id=_id,
        )
    return abort(404)


@app.route(
    "/Tutor/<_id>/Resources/<_id_resource>/Delete/",
    methods=["GET", "POST"],
)
@app.route(
    "/Tutor/<_id>/Resources/<_id_resource>/Delete",
    methods=["GET", "POST"],
)
def tutor_resources_delete(_id, _id_resource):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Tutor" in session:
        results = requests.post(
            "http://127.0.0.1:5000/api/resources",
            {
                "id": int(_id_resource),
            },
        )
        flash("Deleted", "success")
        return redirect(f"/Tutor/{_id}/Resources")
    return abort(404)


@app.route(
    "/Tutor/<_id>/Resources/<_id_resource>/Edit/",
    methods=["GET", "POST"],
)
@app.route(
    "/Tutor/<_id>/Resources/<_id_resource>/Edit",
    methods=["GET", "POST"],
)
def tutor_resources_edit(_id, _id_resource):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Tutor" in session:
        if request.method == "POST":
            method_of_resource = request.form["method-of-resource"]
            link_of_resource = request.form["link-of-resource"]
            title = request.form["Title"]
            description = request.form["Description"]
            # "UPDATE Resources SET title='ttt' WHERE ID=7;"
            results = requests.get(
                "http://127.0.0.1:5000/api/azure/sql",
                {
                    "Query": f"UPDATE Resources SET method_of_resource='{method_of_resource}', link_of_resource='{link_of_resource}', title='{title}', description='{description}' WHERE ID={_id_resource}",
                    "Type": "Insert",
                },
            ).json()
            flash("Updated resources", "success")
            return redirect(f"/Tutor/{_id}/Resources")
        results = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": f"SELECT * FROM Resources WHERE ID = {_id_resource}", "Type": "Select"},
        ).json()["message"][0]
        return render_template(
            "tutor/resources.html",
            method_of_resource=str(results[1]),
            link_of_resource=results[2],
            description=results[3],
            title=results[4],
            _id=_id,
        )
    return abort(404)


@app.route("/Tutor/<_id>/Question/Post", methods=["POST"])
@app.route("/Tutor/<_id>/Question/Post/", methods=["POST"])
def tutor_question_post(_id):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    flash("Question Added", "success")
    request_form = eval(list(dict(request.form).keys())[0] + list(dict(request.form).values())[0])
    print(request_form)
    info = request_form["info"]
    yourdiv = request_form["yourdiv"]
    name = info["name"]
    del info["name"]
    soup = BeautifulSoup(yourdiv, "html.parser")
    for idx in range(len(info)):
        idx = idx + 1
        element = soup.find("input", id=f"{idx}-Input-Name")
        try:
            element.replaceWith(info[str(idx)][0])
        except Exception as e:
            warnings.filterwarnings(e)
        element = soup.find("button")
        try:
            element.string = ""
        except Exception as e:
            warnings.filterwarnings(e)
        try:
            element.unwrap()
        except Exception as e:
            warnings.filterwarnings(e)  # TODO Change Make if else statment
        element = soup.find("div", id=f"{idx}")
        print(element.attrs)
        try:
            del element.attrs['class"mb-3"']
        except Exception as e:
            warnings.filterwarnings(e)
        try:
            element.attrs["class"] = "mb-3"
        except Exception as e:
            warnings.filterwarnings(e)
        element = soup.find("hr")
        element.unwrap()
        inputs = soup.find_all("input", id=f"{idx}-Label")
        for input_ in inputs:
            input_.attrs["answer"] = info[str(idx)][1]
            input_.attrs["name"] = input_.attrs["id"]
    returned_vals = requests.post(
        "http://127.0.0.1:5000/api/questions", {"html": str(soup), "name": str(name)}
    ).json()
    return ("", 200)


@app.route("/Tutor/<_id>/Question/<_id_question>/Preview/")
@app.route(
    "/Tutor/<_id>/Question/<_id_question>/Preview",
)
def tutor_question_preview(_id, _id_question):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Tutor" in session:
        results = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": f"SELECT * FROM Questions WHERE ID = {_id_question}", "Type": "Select"},
        ).json()["message"][0]
        return render_template("tutor/tutor_question_preview.html", code=results[1], _id=_id)
    return abort(404)


@app.route("/Tutor/<_id>/Question/<_id_question>/Delete/")
@app.route(
    "/Tutor/<_id>/Question/<_id_question>/Delete",
)
def tutor_question_delete(_id, _id_question):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Tutor" in session:
        results = requests.get(
            "http://127.0.0.1:5000/api/azure/sql",
            {"Query": f"DELETE FROM Questions WHERE ID={_id_question}", "Type": "Insert"},
        ).json()
        flash("Deleted", "success")
        return redirect(f"/Tutor/{_id}/Question")
    return abort(404)


@app.route("/Tutor/<_id>/Test")
def tutor_test(_id):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return render_template("tutor/test.html", _id=_id)


@app.route("/Tutor/<_id>/Log/Out", methods=["GET", "POST"])
@app.route("/Tutor/<_id>/Log/Out/", methods=["GET", "POST"])
def tutor_log_out(_id):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if "Is_Tutor" in session:
        session.pop("Is_Tutor")
        session.pop("id")
        session.pop("User Name")
        session.pop("Email")
        session.pop("Rank")
        session.pop("Password")
        session.pop("Remember Password")
        session.pop("Enabled")
        session.pop("Phone Number")
        session.pop("Full Name")
        session.pop("Profile Picture")
        session.pop("Qualification")
        session.pop("Description")
        flash("Loged out as tutor", "success")
        return redirect("/")
    return abort(404)
