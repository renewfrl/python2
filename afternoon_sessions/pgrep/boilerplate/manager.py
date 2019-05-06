#!/usr/bin/env python3

from flask_script import Manager
from flask import Flask
from task import whatever

# use Flask framework
app = Flask(__name__)


manager = Manager(app)

@manager.command
def find_in_file(args):
    print("looking for {}".format(args))
    whatever()
    # and print htem


if __name__ == "__main__":
    manager.run()
