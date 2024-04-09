#!/usr/bin/env python3
"""Basic Flask app Module
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def home():
    """Home page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)