import os
import sys

import homepage.views;

from homepage import app

if __name__ == "__main__":
    _package_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _package_path not in sys.path:
        sys.path.insert(0, _package_path)

    homepage.app.run(host="::1", debug=True)
