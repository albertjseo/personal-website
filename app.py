from flask import Flask, render_template, request
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