from flask import Blueprint, Flask


class Vue:
    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("FLASK_VUE_COMPONENT_DIRECTORY", "components")

        self.register_vue_static_url(app)

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
