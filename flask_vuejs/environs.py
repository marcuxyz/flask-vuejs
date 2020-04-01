from flask import current_app, url_for
from markupsafe import Markup


def load_component_file(filename):
    component = current_app.config["FLASK_VUE_COMPONENT_DIRECTORY"]
    f = url_for("static", filename=f"{component}/{filename}.js")
    return Markup(f"<script src='{f}'></script>")
