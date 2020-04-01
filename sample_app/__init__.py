from flask import Flask, render_template
from flask_vuejs import Vue


def create_app():
    app = Flask(__name__)
    Vue(app)

    @app.route("/")
    def form():
        return render_template("form.html")

    return app
