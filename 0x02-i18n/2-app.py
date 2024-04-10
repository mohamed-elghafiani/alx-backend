#!/usr/bin/env python3
"""Basic Flask app Module
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Config variables
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get local user language
    """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale

    return request.accept_languages.best_match(['de', 'fr', 'en'])


@app.route("/")
def home():
    """Home page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
