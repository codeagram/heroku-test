from flask import Flask


def init_app():

    app = Flask(__name__)

    with app.app_context():
        from application.views import base_bp

        app.register_blueprint(base_bp)

    return app
