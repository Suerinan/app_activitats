from flask import Flask

from .routes import UserRoutes, ActivityRoutes, UserActivityRoutes

app = Flask(__name__)

def init__app(config):
    app.config.from_object(config)

    app.register_blueprint(UserRoutes.main, url_prefix='/appActivitats/user')
    app.register_blueprint(ActivityRoutes.main, url_prefix='/appActivitats/activity')
    app.register_blueprint(UserActivityRoutes.main, url_prefix='/appActivitats/sign_user_activity')

    return app