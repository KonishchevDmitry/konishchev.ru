import os
import sys

_package_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _package_path not in sys.path:
    sys.path.insert(0, _package_path)

import homepage
import homepage.views;

if __name__ == "__main__":
    homepage.app.run(host="::1", debug=True)
