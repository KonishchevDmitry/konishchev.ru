import datetime
from setuptools import find_packages, setup

setup(
    name="homepage",
    version=datetime.datetime.today().strftime("%Y.%m.%d-%H.%M.%S"),

    install_requires=["Flask", "Flask-Babel"],

    packages = find_packages(),
    # TODO: external favicons + MANIFEST.in
    package_data={ "homepage": [
        "homepage.ini",
        "static/*/*",
        "templates/*.html",
        "translations/*/LC_MESSAGES/messages.mo",
    ]},
)
