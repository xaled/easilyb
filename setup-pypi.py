#!/usr/bin/env python3
from setup import VERSION
import os
os.system("python3 setup.py sdist && twine upload dist/easilyb-%s.tar.gz"
          " && sudo python3 -m pip install -U easilyb" % VERSION)
