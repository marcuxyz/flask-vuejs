from flask import Blueprint, Flask
from flask_assets import Bundle, Environment

from . import environs


class Vue:
    def __init__(self, app: Flask) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("FLASK_VUE_COMPONENT_DIRECTORY", "components")

        self.register_vue_static_url(app)
        self.register_global_object(app)
        self.build_js(app)

    def register_vue_static_url(self, app):
        app.register_blueprint(
            Blueprint(
                "vue",
                __name__,
                static_url_path=app.static_url_path + "/vue",
                static_folder="static",
                template_folder="templates",
            )
        )

    def register_global_object(self, app):
        app.jinja_env.globals["use_component"] = environs.load_component_file

    def build_js(self, app):
        environ = Environment(app)
        js = Bundle(
            "vue/core/vue.js",
            "vue/core/axios.js",
            "vue/core/config.js",
            output="vue/main.js",
        )
        environ.register("build_js", js)
