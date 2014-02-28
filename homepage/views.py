from collections import namedtuple

from flask import request
from flask.ext.babel import _

from homepage import app
from homepage import util

@app.route("/")
@util.templated("index.html")
def index():
    full_name = _("Dmitry Konishchev")
    Contact = namedtuple("Contact", ("name", "url", "title", "itemprop"))

    return {
        "keywords": full_name + ", " + _("profile"),
        "description": _("Developer at CROC Incorporated | Russian Federation"),

        "full_name": full_name,
        "location": _("Moscow Region, Russian Federation"),
        "occupation": _("Developer at CROC Incorporated"),

        "contacts": [
            Contact("gmail",    "mailto:konishchev@gmail.com",                "konishchev@gmail.com",          "email"),
            Contact("gplus",    "https://www.google.com/+DmitryKonishchev",   "Google+",                       "url"  ),
            Contact("github",   "https://github.com/KonishchevDmitry",        "GitHub",                        "url"  ),
            Contact("vk",       "https://vk.com/konishchevdmitry",            _("VK"),                         "url"  ),
            Contact("twitter",  "https://twitter.com/konishchev",             "Twitter",                       "url"  ),
            Contact("linkedin", "https://www.linkedin.com/in/konishchev",     "LinkedIn",                      "url"  ),
            Contact("moikrug",  "https://konishchevdmitry.moikrug.ru/",       "Мой Круг",                      "url"  ),
            Contact("facebook", "https://www.facebook.com/dmitry.konishchev", "Facebook",                      "url"  ),
            Contact("blogger",  "https://konishchevdmitry.blogspot.com/",     "KonishchevDmitry's small blog", "url"  ),
        ],
    }

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("images/" + request.path[1:])

@app.route("/googlee5c41083383fc5e9.html")
@app.route("/yandex_4620d67a71b3484a.html")
def robots():
    return app.send_static_file("robots/" + request.path[1:])
