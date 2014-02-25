from flask import request
from flask.ext.babel import _

from homepage import app
from homepage import util

@app.route("/")
@util.templated("index.html")
def index():
    full_name = _("Dmitry Konishchev")

    return {
        "lang": util.get_locale(),
        "keywords": full_name + ", " + _("profile"),
        "description": _("Developer at CROC Incorporated | Russian Federation"),
        "full_name": full_name,

        "location": _("Moscow Region, Russian Federation"),
        "occupation": _("Developer at CROC Incorporated"),
        "contacts": [
            ( "gmail",    "mailto:konishchev@gmail.com",                "Email"    ),
            ( "gplus",    "https://www.google.com/+DmitryKonishchev",   "Google+"  ),
            ( "github",   "https://github.com/KonishchevDmitry",        "GitHub"   ),
            ( "vk",       "https://vk.com/konishchevdmitry",            _("VK")    ),
            ( "twitter",  "https://twitter.com/konishchev",             "Twitter"  ),
            ( "linkedin", "https://www.linkedin.com/in/konishchev",     "LinkedIn" ),
            ( "moikrug",  "https://konishchevdmitry.moikrug.ru/",       "Мой Круг" ),
            ( "facebook", "https://www.facebook.com/dmitry.konishchev", "Facebook" ),
            ( "blogger",  "https://konishchevdmitry.blogspot.com/",     "KonishchevDmitry's small blog" ),
        ],
    }

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("images/" + request.path[1:])

@app.route("/googlee5c41083383fc5e9.html")
@app.route("/yandex_4620d67a71b3484a.html")
def robots():
    return app.send_static_file("robots/" + request.path[1:])
