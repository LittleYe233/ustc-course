#!/usr/bin/env python3

from app import app
from app import db
from random import randint
from app.models import Review, Course, Student, User
import argparse


VERSION = 'ustc-course (forked) v0.1.0'  # should follow Semantic Versioning


# parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', help='run the server in debug mode',
                    action='store_true')
parser.add_argument('-H', '--host', type=str, default='0.0.0.0',
                    help='set host of the server (default value: 0.0.0.0)')
parser.add_argument('-p', '--port', type=int, default=8080,
                    help='set port of the server (default value: 8080)')
parser.add_argument('-v', '--version', help='print the version string',
                    action='store_true')
args = parser.parse_args()

if args.version:
    print(VERSION)
    exit(0)


# set up the server
def start():
    if args.debug:
        db.create_all()
    # default `processes` is 4, raising ValueError
    app.run(port=args.port, processes=True, host=args.host)


# Main function
if __name__ == '__main__':
    start()
