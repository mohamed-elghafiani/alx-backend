#!/usr/bin/env python3
"""Basic Flask app Module
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel, format_datetime
import pytz
from datetime import datetime


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
        return users.get(user_id, None)


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
    elif getattr(g, 'user', None):
        user = getattr(g, 'user', None)
        if user["locale"] in app.config['LANGUAGES']:
            return user["locale"]
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ get timezone from request. """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """Home page"""
    timezone = get_timezone()
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    current_time = format_datetime(datetime=current_time)
    return render_template("index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
