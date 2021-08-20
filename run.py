#!/usr/bin/env python3
from app import app
from app import db
from random import randint
from app.models import Review, Course, Student, User
import sys

debug = False
for arg in sys.argv:
    if arg == '-d':
        debug = True

def start():
    if debug:
        db.create_all()
        # default process = 4, raising ValueError
        app.run(port=8080, processes=True, host='0.0.0.0')
    else:
        app.run(port=3000, processes=True)



if __name__ == '__main__':
    start()
