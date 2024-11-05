#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel, _

class Config:
    """
    Language configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    """
    The base route
    """
    return render_template('2-index.html')

@babel.localeselector
def get_locale():
    """
    Locale selector
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
