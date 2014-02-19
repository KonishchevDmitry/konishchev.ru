from functools import wraps

from flask import render_template

def templated(template_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ctx = f(*args, **kwargs) or {}
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator
