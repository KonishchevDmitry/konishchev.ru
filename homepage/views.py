from flask import request

from homepage import app
from homepage import util

@app.route("/")
@util.templated("index.html")
def index():
    return { "lang": util.get_locale() }

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("images/" + request.path[1:])

@app.route("/googlee5c41083383fc5e9.html")
@app.route("/yandex_4620d67a71b3484a.html")
def robots():
    return app.send_static_file("robots/" + request.path[1:])
