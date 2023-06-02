"""hackday package initializer."""
import flask
# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name
# Read settings from config module (hackday/config.py)
app.config.from_object('hackday.config')
# Overlay settings read from a Python file whose path is set in the environment
# variable hackday_SETTINGS. Setting this environment variable is optional.
# Docs: http://flask.pocoo.org/docs/latest/config/
#
# EXAMPLE:
# $ export hackday_SETTINGS=secret_key_config.py
app.config.from_envvar('hackday_SETTINGS', silent=True)
# Tell our app about views and model.  This is dangerously close to a
# circular import, which is naughty, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/patterns/packages/)  We're
# going to tell pylint and pycodestyle to ignore this coding style violation.
import hackday.views  # noqa: E402  pylint: disable=wrong-import-position
import hackday.model  # noqa: E402  pylint: disable=wrong-import-position
import hackday.api  # noqa: E402  pylint: disable=wrong-import-position
import hackday.utils # noqa: E402  pylint: disable=wrong-import-position
import hackday.credentials # noqa: E402  pylint: disable=wrong-import-position
