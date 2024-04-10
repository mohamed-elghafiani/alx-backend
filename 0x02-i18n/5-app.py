#!/usr/bin/env python3
"""Basic Flask app Module
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Config Variables
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Return current loged in user or None
    """
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """Set current user as a global variable
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Get user local language or return default language
    """
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale
    else:
        user = getattr(g, 'user', None)
        if user is not None:
            return user.locale

    return request.accept_languages.best_match(['en', 'fr'])


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """Home page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
