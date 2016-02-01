#!/home1/ftwopict/public_html/F2Pictures/bin/python

import sys
import os

sys.path.insert(0, "/home1/ftwopict/public_html/F2Pictures/lib/python3.5/site-packages")
sys.path.insert(1, "/home1/ftwopict/public_html/F2Pictures/")
sys.path.append("/home1/ftwopict/www/F2Pictures")
sys.path.append("/home1/ftwopict/www/F2Pictures/F2Pictures")

#Using Cookie Cuttr Project Layout

os.environ["DJANGO_SETTINGS_MODULE"] = "F2Pictures.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
