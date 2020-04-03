from os import environ

from flask import Blueprint, Flask

from . import commands


class Vue:
    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        commands.init_app(app)
        self.register_vue_blueprint(app)

        app.config.setdefault(
            "FLASK_APPLICATION_PATH", environ.get("FLASK_APPLICATION_PATH", ".")
        )

    def register_vue_blueprint(self, app):
        app.register_blueprint(
            Blueprint(
                "vue",
                __name__,
                static_url_path=app.static_url_path + "/vue",
                static_folder="static",
                template_folder="templates",
            )
        )
