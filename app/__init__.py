from flask import Flask


def create_app():
    app = Flask(__name__)

    from .controllers.pricing_controller import pricing_bp
    app.register_blueprint(pricing_bp)

    return app
