from flask import Flask, render_template
from markupsafe import Markup

app = Flask(__name__)


@app.route('/')
def home():
    page = render_template("home.html")
    return render_template("base.html", content=Markup(page))


#@app.route('/experiences', methods=["GET"])
#def experience():
#    page = render_template("experiences.html")
#    return render_template("base.html", content=Markup(page))


@app.route('/projects', methods=["GET"])
def project():
    page = render_template("projects.html")
    return render_template("base.html", content=Markup(page))


@app.route('/about_me', methods=["GET"])
def aboutme():
    page = render_template("about_me.html")
    return render_template("base.html", content=Markup(page))


@app.route('/contact', methods=["GET"])
def contact():
    page = render_template("contact.html")
    return render_template("base.html", content=Markup(page))


@app.route('/covid_sql', methods=["GET"])
def project1():
    page = render_template("individual_projects/covid_sql.html")
    return render_template("base.html", content=Markup(page))


@app.route('/valorant_tracker', methods=["GET"])
def project2():
    page = render_template("individual_projects/valorant_tracker.html")
    return render_template("base.html", content=Markup(page))


@app.route('/agm_db', methods=["GET"])
def project3():
    page = render_template("individual_projects/agm_db.html")
    return render_template("base.html", content=Markup(page))


@app.route('/cell_morphology', methods=["GET"])
def project4():
    page = render_template("individual_projects/cell_morphology.html")
    return render_template("base.html", content=Markup(page))


@app.route('/drug_discovery', methods=["GET"])
def project5():
    page = render_template("individual_projects/drug_discovery.html")
    return render_template("base.html", content=Markup(page))


if __name__ == '__main__':
    app.run(debug=True)
