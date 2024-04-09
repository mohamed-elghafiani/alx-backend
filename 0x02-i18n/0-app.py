#!/usr/bin/env python3
"""Basic Flask app Module
"""
from flask import Flask, render_template


app = Flask(__name__)


def home():
    """Home page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)