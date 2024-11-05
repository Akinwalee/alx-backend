#!/usr/bin/env python3

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    Get user
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None

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

@app.before_request
def before_request():
    g.user = get_user()

@app.route('/')
def index():
    """
    The base route
    """
    return render_template('7-index.html')


def get_timezone():
    """
    1. Check for timezone in URL parameters
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # Validate the time zone
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    # 2. Check for user's timezone
    if g.user and g.user.get('timezone'):
        try:
            # Validate user's time zone
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass

    # 3. Fall back to the default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']

babel.timezoneselector(get_timezone)

@babel.localeselector
def get_locale():
    """
    Locale selector
    """
    if g.user and g.user['locale']:
        return g.user['locale']
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
