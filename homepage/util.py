from functools import wraps

from flask import render_template, request

from homepage import babel

@babel.localeselector
def get_locale():
    supported_locales = ("ru", "en")

    locale = request.args.get("lang")
    if locale in supported_locales:
        return locale

    return request.accept_languages.best_match(supported_locales) \
        or supported_locales[0]

def templated(template_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ctx = f(*args, **kwargs) or {}
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator
