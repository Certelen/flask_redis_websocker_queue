#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/test")
from main import app as application
application.secret_key = 'ed4eedsewsdfruf74hf'